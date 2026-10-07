# Rocky Linux

## 地址

<https://mirrors.ustc.edu.cn/rocky/>

## 说明

Rocky Linux 软件源

## 收录架构

x86_64, aarch64

## 收录版本

8, 9, 10

## 使用说明

!!! warning

    操作前请做好相应备份。

=== "Rocky Linux 8"

    使用以下命令替换默认的配置：

    ```shell
    sed -e 's|^mirrorlist=|#mirrorlist=|g' \
        -e 's|^#baseurl=http://dl.rockylinux.org/$contentdir|baseurl=https://mirrors.ustc.edu.cn/rocky|g' \
        -i.bak \
        /etc/yum.repos.d/Rocky-AppStream.repo \
        /etc/yum.repos.d/Rocky-BaseOS.repo \
        /etc/yum.repos.d/Rocky-Extras.repo \
        /etc/yum.repos.d/Rocky-PowerTools.repo
    ```

=== "Rocky Linux 9/10"

    使用以下命令替换默认的配置：

    ```shell
    sed -e 's|^mirrorlist=|#mirrorlist=|g' \
        -e 's|^#baseurl=http://dl.rockylinux.org/$contentdir|baseurl=https://mirrors.ustc.edu.cn/rocky|g' \
        -i.bak \
        /etc/yum.repos.d/rocky-extras.repo \
        /etc/yum.repos.d/rocky.repo
    ```

以上命令只替换了默认启用的仓库。替换之后请运行 `dnf makecache` 更新缓存。

内网中有多台机器时，请参考 [使用 Nginx 搭建内网镜像缓存](mirror-cache.md#rocky-linux)，减少软件包和元数据的重复下载流量。**由于 Rocky 元数据带来的流量压力过大，我们可能封禁或限速大量访问 Rocky 元数据的网段。**

## 相关链接

官方主页

:   <https://rockylinux.org/>

论坛

:   <https://forums.rockylinux.org/>

文档

:   <https://docs.rockylinux.org/>

Wiki

:   <https://wiki.rockylinux.org/>

镜像列表

:   <https://mirrors.rockylinux.org/mirrormanager/mirrors>
