# 镜像站搭建简要教程

!!! warning "本部分需要验证与进一步扩充"

开始前先阅读 <https://github.com/tuna/tunasync/wiki/Mirroring-Howto>。

假设 repo 总目录在 `/srv/repo`。

## Yuki

<https://github.com/ustclug/yuki?tab=readme-ov-file#quickstart>

假设镜像配置在 `/home/mirror/repos`，同步日志在 `/home/mirror/logs`，对应修改 `daemon.toml` 中 `repo_logs_dir` 和 `repo_config_dir`。同时范例中的 docker-ce 同步配置就位于 `/home/mirror/repos/docker-ce.yaml`，内容如下：

```yaml
name: docker-ce
# every 1 hour
cron: "0 * * * *"
storageDir: /srv/repo/docker-ce
image: ustcmirror/rsync:latest
logRotCycle: 2
envs:
  RSYNC_HOST: rsync.mirrors.ustc.edu.cn
  RSYNC_PATH: docker-ce/
  RSYNC_EXCLUDE: --exclude=.~tmp~/
  RSYNC_EXTRA: --size-only
  RSYNC_MAXDELETE: "50000"
```

如果需要快速获取仓库大小：

- ZFS: 需要创建 dataset 挂载到 /srv/repo/docker-ce
- XFS: 需要为 /srv/repo/docker-ce 设置 quota，可阅读 <https://201.ustclug.org/ops/storage/filesystem/#xfs>
- 其他：不支持

并参考 <https://github.com/ustclug/Yuki/blob/main/cmd/yukid/README.md#server-configuration> 调整 daemon.toml。

## Homepage

<https://git.lug.ustc.edu.cn/mirrors/mirrors-index>

1. clone 后 `git submodule update --init --recursive`
2. 安装对应 Python 依赖（requests, jinja2）
3. 添加 crontab 定时运行，输出到 `/srv/repo/index.html`

如果需要状态页，参考 <https://git.lug.ustc.edu.cn/mirrors/mirrors-index/-/blob/master/status/genstatus.py>

## Nginx（HTTP 服务）

最简单的 nginx 配置直接将 root 设置为 `/srv/repo`，并添加 `autoindex on` 即可。

## Rsyncd（Rsync 服务）

一般而言，对内部提供服务的镜像站只需要配置 HTTP 服务。
如果需要允许其他镜像站作为下游同步，才需要配置 rsync 服务。

??? tip "rsync-huai"

    对于机械硬盘阵列，TUNA 的 @shankerwangmiao 有个优化 patch: <https://github.com/tuna/rsync/blob/master/README-huai.md>，具体而言，需要在 SSD 上创建一个 ReiserFS 分区，然后每次同步完成之后将所有文件元数据同步到这个分区上，然后 patch 过的服务端会先读取 SSD 上的元数据，从而降低机械硬盘压力。

    我们曾在 <https://github.com/ustclug/rsync> 自行维护一个 fork，应用到较新的 rsync 版本上。

作为 quickstart，这里只介绍 Debian rsync 的配置。服务依赖于创建 `/etc/rsyncd.conf`：

```console
$ cat /lib/systemd/system/rsync.service
[Unit]
Description=fast remote file copy program daemon
ConditionPathExists=/etc/rsyncd.conf
After=network.target
Documentation=man:rsync(1) man:rsyncd.conf(5)
（省略）
```

因此需要创建对应的文件，一个参考配置如下：

```conf
pid file = /var/run/rsyncd.pid
log file = /var/log/rsyncd.log

max verbosity = yes
transfer logging = yes
ignore nonreadable = yes
uid = nobody
gid = nogroup
use chroot = yes
dont compress = *
max connections = 60
refuse options = checksum
read only = true
timeout = 240
list = no
reverse lookup = no

[docker-ce]
path = /srv/repo/docker-ce
```
