# CentOS

## 地址

<https://mirrors.ustc.edu.cn/centos/>

## 说明

CentOS 软件源

## 收录架构

x86_64, aarch64, ppc64le

## 收录版本

7

!!! warning

    不受支持的版本已被官方移除出该仓库。如有需要，请使用 [centos-vault](https://mirrors.ustc.edu.cn/centos-vault/) 镜像，并自行替换对应的 URL。

    CentOS 7 将于 2024 年 6 月 30 日结束维护，我们强烈建议尽快迁移到其他解决方案。关于镜像仓库后续处理，请阅读 [CentOS 仓库即将结束服务 (2024-06-30)](https://servers.ustclug.org/2024/05/centos-eol/)。

    CentOS 9 Stream 及以后的版本的镜像位于 [centos-stream](https://mirrors.ustc.edu.cn/centos-stream/)，详见 [centos-stream 帮助页](./centos-stream.md)。

## 使用说明

!!! warning

    操作前请做好相应备份。

对于 CentOS 7，使用以下命令替换默认配置

    sudo sed -e 's|^mirrorlist=|#mirrorlist=|g' \
             -e 's|^#baseurl=http://mirror.centos.org/centos|baseurl=https://mirrors.ustc.edu.cn/centos|g' \
             -i.bak \
             /etc/yum.repos.d/CentOS-Base.repo

以上命令只替换了默认启用的仓库。替换之后请运行 `yum makecache` 更新缓存。

以下是替换之后的文件：

- CentOS 7：

    `/etc/yum.repos.d/CentOS-Base.repo`
    文件：

    ```ini
    --8<-- "centos7/CentOS-Base.repo"
    ```

## 相关链接

官方主页

:   <https://www.centos.org/>

邮件列表

:   <https://wiki.centos.org/zh/GettingHelp/ListInfo>

论坛

:   <https://forums.centos.org/>

文档

:   <https://docs.centos.org/>

Wiki

:   <https://wiki.centos.org/zh/>

镜像列表

:   <https://www.centos.org/download/mirrors/>
