# 使用 Nginx 搭建内网镜像缓存

如果内网中有多台机器，可以使用一台 Nginx 服务器缓存软件源，让相同文件的后续请求从内网获取，减少外网流量。客户端将软件源地址指向缓存服务器；缓存未命中时，服务器从上游获取文件，后续请求则可以复用已经下载的内容。

本文采用按需缓存，不预先同步整个仓库。如果需要完整镜像或离线使用，请参考 [rsync 同步帮助](rsync-guide.md)。**请勿通过遍历下载的方式预热整个仓库。**

## 缓存原则

不同软件源的目录结构和更新方式不同，缓存规则需要分别配置：

- 入口索引通常会在原 URL 上更新，应不缓存或采用适合该仓库的短缓存策略，避免客户端长时间看不到更新。
- 路径包含内容哈希的文件适合长期缓存，即使入口索引更新，相同文件也可以继续复用。
- 软件包是否可以长期缓存，取决于上游是否可能在同一 URL 上替换内容，不能只根据文件扩展名判断。
- 合并同一文件的并发回源请求，可以减少多台机器同时更新时的重复下载。
- 缓存服务器只向需要使用它的内网开放，并保留客户端原有的签名、哈希校验等机制。

本文目前提供 Rocky Linux 软件源缓存的配置实例。Ubuntu、PyPI 等软件源的索引和下载路径不同，需要各自的缓存规则与客户端设置，不能直接套用 Rocky 的配置。

## 公共准备

### 环境

缓存服务器可以使用 Ubuntu、Debian 或 Rocky Linux 等 Linux 发行版。缓存服务器的发行版不需要与客户端相同，例如可以在 Debian 上缓存 Rocky Linux 软件源。

| 项目 | 示例值 |
| --- | --- |
| 缓存服务器内网地址 | `192.168.10.2` |
| 允许访问的客户端网段 | `192.168.10.0/24` |

请按实际情况修改地址和网段。缓存服务器需要能够访问上游镜像，并有足够的磁盘空间；缓存容量限制由 Nginx 后台清理维护，磁盘还需为临时下载等预留空间。

以下管理命令以 root 身份执行。示例在可信内网中提供 HTTP 服务，上游连接使用 HTTPS 并验证证书。

### 安装 Nginx

在缓存服务器上，按发行版选择安装命令：

=== "Ubuntu / Debian"

    ```shell
    apt update
    apt install nginx ca-certificates
    ```

=== "Rocky Linux"

    ```shell
    dnf install nginx ca-certificates
    ```

    如果启用了 SELinux，允许 Nginx 连接上游：

    ```shell
    setsebool -P httpd_can_network_connect on
    ```

使用发行版自带的软件包时，以下默认值有所不同：

| 缓存服务器系统 | Nginx 运行用户及组 | CA 证书路径 |
| --- | --- | --- |
| Ubuntu / Debian | `www-data:www-data` | `/etc/ssl/certs/ca-certificates.crt` |
| Rocky Linux | `nginx:nginx` | `/etc/pki/tls/certs/ca-bundle.crt` |

后面的配置默认使用 Rocky Linux 的证书路径。在 Ubuntu、Debian 上使用时，请将 `proxy_ssl_trusted_certificate` 改为表中对应的路径。如果修改过 Nginx 运行用户，请以 `/etc/nginx/nginx.conf` 中的 `user` 配置为准。

不熟悉 Nginx 配置结构时，可以先阅读 [Linux 201：Nginx 服务器](https://201.ustclug.org/ops/network-service/nginx/)，其中介绍了配置文件、虚拟主机、反向代理和缓存的基本用法。

## Rocky Linux

本节适用于 Rocky Linux 8、9、10 客户端。

Rocky Linux 默认安装的 DNF 定时任务会在后台刷新元数据。检查仓库并不意味着每次都下载全部元数据，但当仓库入口 `repomd.xml` 变化时，DNF 可能重新下载内容没有变化的元数据文件。共享缓存可以减少这些重复下载，也可以缓存多台机器安装的相同 RPM 包。

### 配置缓存

本例使用 `https://mirrors.ustc.edu.cn/rocky/` 作为上游，在 `/var/cache/nginx/rocky` 保存最多约 50 GiB 缓存，可根据实际情况调整。先创建缓存目录；启用 SELinux 时还需恢复新目录的默认标签：

=== "Ubuntu / Debian"

    ```shell
    install -d -o www-data -g www-data -m 0750 /var/cache/nginx/rocky
    ```

=== "Rocky Linux"

    ```shell
    install -d -o nginx -g nginx -m 0750 /var/cache/nginx/rocky
    ```

    启用 SELinux 时执行：

    ```shell
    restorecon -RFv /var/cache/nginx/rocky
    ```

新建 `/etc/nginx/conf.d/rocky-cache.conf`，写入以下内容。上述发行版软件包提供的 `nginx.conf` 会在 `http` 块中包含此目录，以下配置不需要再包一层 `http { ... }`。

请将示例中的 `192.168.10.2` 和 `192.168.10.0/24` 改为实际地址和网段。在 Ubuntu、Debian 上，还需将 `proxy_ssl_trusted_certificate` 的路径改为 `/etc/ssl/certs/ca-certificates.crt`。

```nginx
# 配置缓存路径与大小
proxy_cache_path /var/cache/nginx/rocky
    levels=1:2 keys_zone=rocky_cache:32m
    max_size=50g inactive=30d use_temp_path=off;

# 配置日志格式
log_format rocky_cache '$remote_addr [$time_local] "$request" '
                       '$status $body_bytes_sent cache=$upstream_cache_status '
                       'upstream=$upstream_addr upstream_bytes=$upstream_bytes_received';

server {
    # 监听 IP 地址与端口
    listen 192.168.10.2:80;
    server_name 192.168.10.2;

    # 允许/禁止访问的 IP 范围
    allow 192.168.10.0/24;
    deny all;

    # 日志路径
    access_log /var/log/nginx/rocky-cache.access.log rocky_cache;
    error_log /var/log/nginx/rocky-cache.error.log;

    # 发送给上游（镜像站）的 HTTP 头信息
    proxy_set_header Host mirrors.ustc.edu.cn;
    proxy_set_header Connection "";
    proxy_set_header Accept-Encoding "";
    proxy_http_version 1.1;

    # 验证镜像站 TLS 证书
    proxy_ssl_server_name on;
    proxy_ssl_name mirrors.ustc.edu.cn;
    proxy_ssl_verify on;
    proxy_ssl_trusted_certificate /etc/pki/tls/certs/ca-bundle.crt;
    proxy_ssl_verify_depth 3;

    # 反代相关配置
    proxy_connect_timeout 10s;
    proxy_read_timeout 300s;
    proxy_buffering on;
    proxy_cache_key "$proxy_host$request_uri";
    proxy_cache_lock on;
    proxy_cache_lock_timeout 300s;
    proxy_cache_lock_age 300s;
    proxy_cache_revalidate on;

    # 供调试的 HTTP 头配置
    add_header X-Cache-Status $upstream_cache_status always;

    # 文件名包含 hash 的元数据可以长期缓存
    location ~ "^/rocky/.*/repodata/[0-9a-f]{64}-[^/]+$" {
        limit_except GET HEAD { deny all; }
        proxy_pass https://mirrors.ustc.edu.cn;
        proxy_cache rocky_cache;
        proxy_ignore_headers X-Accel-Expires Expires Cache-Control;
        proxy_cache_valid 200 30d;
    }

    # RPM 按需缓存
    location ~ ^/rocky/.*/Packages/.*\.rpm$ {
        limit_except GET HEAD { deny all; }
        proxy_pass https://mirrors.ustc.edu.cn;
        proxy_cache rocky_cache;
        proxy_cache_valid 200 1d;
    }

    # repomd.xml、签名和其他未匹配的文件缓存 5 分钟
    location /rocky/ {
        limit_except GET HEAD { deny all; }
        proxy_pass https://mirrors.ustc.edu.cn;
        proxy_cache rocky_cache;
        proxy_ignore_headers X-Accel-Expires Expires Cache-Control;
        proxy_cache_valid 200 5m;
    }

    location / {
        return 404;
    }
}
```

配置中有几处需要注意：

- `keys_zone=rocky_cache:32m` 为缓存键和元信息分配共享内存，文件内容保存在磁盘上，容量由 `max_size=50g` 控制。`levels=1:2` 将缓存文件分散到多层目录，避免单个目录内文件过多。
- 上游 HTTP 请求的 `Host` 与 TLS 握手的 SNI 都指向 `mirrors.ustc.edu.cn`，而不是客户端访问的内网地址。如果更换上游，需要同时修改 `proxy_pass`、`proxy_set_header Host` 和 `proxy_ssl_name`。

缓存策略如下：

- **带哈希的元数据**：缓存成功的 `200` 响应 30 天；相同 URL 对应相同内容，因此在此位置忽略上游的缓存有效期响应头。没有访问的条目也可能被清理。
- **RPM 包**：没有上游缓存控制时，缓存成功的 `200` 响应 1 天；上游的缓存控制响应头优先。
- **`repomd.xml` 在内的其他文件**：缓存成功的 `200` 响应 5 分钟，忽略上游的缓存有效期响应头，避免客户端长时间看到旧索引。
- **并发请求**：同一缓存键首次被多个客户端请求时，其他请求等待正在进行的下载，最长等待 300 秒。下载过慢、锁超时或缓存被清理时，仍可能产生重复回源。

缓存没有启用过期内容回退，也没有配置错误响应的缓存时间。不要为整个 `/rocky/` 路径统一设置长缓存，否则可能出现索引陈旧、索引引用的文件已被上游移除等问题。

检查配置并启动服务：

```shell
nginx -t
systemctl enable --now nginx
systemctl reload nginx
```

只有 `nginx -t` 成功后才执行后续命令。如果服务器已有 Nginx 站点，请先检查监听地址和虚拟主机配置是否冲突。

如果启用了 firewalld，先用 `firewall-cmd --get-active-zones` 确认内网接口所在区域。以下以 `public` 区域为例，仅允许示例内网访问 TCP 80 端口：

```shell
firewall-cmd --permanent --zone=public \
    --add-rich-rule='rule family="ipv4" source address="192.168.10.0/24" port port="80" protocol="tcp" accept'
firewall-cmd --reload
```

### 配置客户端

先备份客户端 `/etc/yum.repos.d/` 中的仓库配置文件，再参考 [Rocky Linux 使用帮助](rocky.md) 将软件源改为科大源。然后将配置中的 `https://mirrors.ustc.edu.cn/rocky` 替换为 `http://192.168.10.2/rocky`，保留后面的路径和变量。

修改后刷新客户端缓存：

```shell
dnf clean metadata
dnf makecache
```

### 验证缓存命中

从内网客户端连续执行两次以下命令，请求仓库入口文件并查看响应头。请按实际客户端版本和架构修改路径：

```shell
curl -fsS -D - http://192.168.10.2/rocky/9/BaseOS/x86_64/os/repodata/repomd.xml \
    -o /tmp/rocky-repomd.xml
```

通常第一次响应包含 `X-Cache-Status: MISS`，第二次包含 `X-Cache-Status: HIT`。如果文件已经缓存，第一次也可能是 `HIT`。也可以在另一台内网机器上请求同一 URL，确认能够共享缓存。

如需进一步验证较大的元数据文件，从保存的 `/tmp/rocky-repomd.xml` 中找到 `type="primary"` 对应的 `location href`，得到当前有效的 `repodata/<哈希>-primary.xml.gz` 路径。将它接在仓库根路径后，同样连续请求两次：

```shell
curl -fsS -D - -o /dev/null \
    'http://192.168.10.2/rocky/9/BaseOS/x86_64/os/repodata/<哈希>-primary.xml.gz'
```

请将 `<哈希>` 替换为实际值；旧教程或日志中的文件可能已被上游删除。

查看缓存服务器日志：

```shell
tail -f /var/log/nginx/rocky-cache.access.log
```

`cache=HIT` 表示命中缓存，`MISS` 表示没有命中，`REVALIDATED` 表示过期缓存经上游确认仍有效。判断节省的外网流量应看回源情况，而不是客户端请求数：客户端仍可能重复下载，但数据可以来自内网缓存。

### 维护与排查

- 使用 `du -sh /var/cache/nginx/rocky` 和 `df -h /var/cache/nginx` 查看磁盘使用情况。`inactive=30d` 表示 30 天未被访问的条目可被清理，不表示所有内容都保持新鲜 30 天。
- 同一个文件的请求路径需要一致才能共享缓存。`/rocky/9/` 和 `/rocky/9.8/` 会形成不同的缓存键，建议客户端保留默认 `$releasever`，不要混用手工固定的小版本路径。
- 如果响应为 `403`，检查客户端地址是否在允许网段内。如果响应为 `502`，检查错误日志、服务器 DNS、上游连接、证书及 SELinux 设置。上游域名在此配置加载时解析，上游地址变化后可能需要重新加载 Nginx。
- 如果元数据出现 `404` 或校验错误，先检查上游是否正在同步。上游更新后，缓存中的旧索引可能仍指向已删除的文件。可以等待 5 分钟，让入口文件的缓存过期，再在客户端执行 `dnf clean metadata` 和 `dnf makecache`；如果仍然失败，检查上游对应文件是否可以正常下载。

需要恢复时，将客户端的仓库配置改回备份中的地址或参考 [Rocky Linux 使用帮助](rocky.md)，再执行一次 `dnf clean metadata` 和 `dnf makecache`。

## 相关链接

- [Rocky Linux 使用帮助](rocky.md)
- [Linux 201：Nginx 服务器](https://201.ustclug.org/ops/network-service/nginx/)
- [Nginx HTTP 代理与缓存模块](https://nginx.org/en/docs/http/ngx_http_proxy_module.html)
- [RHEL：配置 Nginx 反向代理及 SELinux](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/deploying_web_servers_and_reverse_proxies/setting-up-and-configuring-nginx_deploying-web-servers-and-reverse-proxies)
- [DNF：makecache 缓存判断问题](https://github.com/rpm-software-management/dnf/issues/2242)
