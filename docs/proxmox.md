# Proxmox

## 地址

<https://mirrors.ustc.edu.cn/proxmox/>

## 说明

Proxmox 软件源

## 收录架构

所有 Proxmox 官方支持的架构

## 收录版本

所有 Proxmox 官方支持的版本

## 使用说明

!!! warning

    操作前请做好相应备份

### Debian，Proxmox

一般情况下，需要同时修改基础系统（Debian）的源文件（`/etc/apt/sources.list` 或 `/etc/apt/sources.list.d/debian.sources`）和 Proxmox 的源文件。

修改基础系统（Debian）的源文件，可以参考 [Debian 帮助](debian.md) 或使用如下命令：

--8<-- "deb822.md"

=== "`sources.list` 格式"

    ```shell
    sed -i 's|^deb http://ftp.debian.org|deb https://mirrors.ustc.edu.cn|g' /etc/apt/sources.list
    sed -i 's|^deb http://security.debian.org|deb https://mirrors.ustc.edu.cn/debian-security|g' /etc/apt/sources.list
    ```

=== "DEB822 格式"

    ```shell
    sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list.d/debian.sources
    ```

    目前 Debian Bookworm 及以后的容器镜像和 Debian Trixie 已经使用 DEB822 格式，且其安全更新源默认设置为 `http://deb.debian.org/debian-security`，因此以上命令会同时替换 Debian 官方源和安全更新源。

修改 Proxmox 的源文件，可以使用如下命令：

{% for release in debian_releases %}
{% if release.proxmox_version %}
=== "Proxmox VE {{ release.proxmox_version }}"

    === "`sources.list` 格式"

        ```shell
        echo "deb https://mirrors.ustc.edu.cn/proxmox/debian/pve {{ release.codename }} pve-no-subscription" > /etc/apt/sources.list.d/pve-no-subscription.list
        ```

    === "DEB822 格式"

        ```shell
        cat > /etc/apt/sources.list.d/pve-no-subscription.sources <<EOF
        Types: deb
        URIs: https://mirrors.ustc.edu.cn/proxmox/debian/pve
        Suites: {{ release.codename }}
        Components: pve-no-subscription
        Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
        EOF
        ```

{% endif %}
{% endfor %}

对于 Proxmox Backup Server 和 Proxmox Mail Gateway，请将以上命令中的 `pve` 分别替换为 `pbs` 和 `pmg`。

PVE 8 之后默认安装 Ceph 仓库源文件 `/etc/apt/sources.list.d/ceph.list` 或 `/etc/apt/sources.list.d/ceph.sources`，可以使用如下命令更换源：

=== "`sources.list` 格式"

    ```shell
    if [ -f /etc/apt/sources.list.d/ceph.list ]; then
      CEPH_CODENAME=`ceph -v | grep ceph | awk '{print $(NF-1)}'`
      source /etc/os-release
      echo "deb https://mirrors.ustc.edu.cn/proxmox/debian/ceph-$CEPH_CODENAME $VERSION_CODENAME no-subscription" > /etc/apt/sources.list.d/ceph.list
    fi
    ```

=== "DEB822 格式"

    ```shell
    if [ -f /etc/apt/sources.list.d/ceph.sources ]; then
      CEPH_CODENAME=`ceph -v | grep ceph | awk '{print $(NF-1)}'`
      source /etc/os-release
      cat > /etc/apt/sources.list.d/ceph.sources <<EOF
    Types: deb
    URIs: https://mirrors.ustc.edu.cn/proxmox/debian/ceph-$CEPH_CODENAME
    Suites: $VERSION_CODENAME
    Components: no-subscription
    Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
    EOF
    fi
    ```

更改完 `sources.list` 或 DEB822 仓库描述文件后请运行 `apt update` 更新索引以生效。

### CT Templates

另外，如果你需要使用 Proxmox 网页端或 `pveam` 命令下载 CT Templates，可以替换 CT Templates 的源为 `http://mirrors.ustc.edu.cn`。

具体方法：将 `/usr/share/perl5/PVE/APLInfo.pm` 文件中默认的源地址 `http://download.proxmox.com` 替换为 `https://mirrors.ustc.edu.cn/proxmox` 即可。

可以使用如下命令：

```shell
sed -i.bak 's|http://download.proxmox.com|https://mirrors.ustc.edu.cn/proxmox|g' /usr/share/perl5/PVE/APLInfo.pm
```

针对 `/usr/share/perl5/PVE/APLInfo.pm` 文件的修改，执行 `systemctl restart pvedaemon` 后生效。

!!! note

    `/usr/share/perl5/PVE/APLInfo.pm` 文件属于 pve-manager 软件包，该软件包升级后，需要重新替换 URL。
