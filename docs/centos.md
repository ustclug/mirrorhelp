# CentOS

## 地址

<https://mirrors.ustc.edu.cn/centos/>

## 说明

CentOS 软件源

## 收录架构

x86_64, aarch64, ppc64le

## 收录版本

7, 8 Stream

:::: warning
::: title
Warning
:::

CentOS 8（非 Stream 版本）已被官方移除出该仓库。如有需要，请使用
[centos-vault](https://mirrors.ustc.edu.cn/centos-vault/) 镜像。

CentOS 9 Stream 及以后的版本的镜像位于
[centos-stream](https://mirrors.ustc.edu.cn/centos-stream/)。
::::

## 使用说明

:::: warning
::: title
Warning
:::

操作前请做好相应备份。
::::

对于 CentOS 8 Stream，使用以下命令替换默认的配置

    sudo sed -e 's|^mirrorlist=|#mirrorlist=|g' \
             -e 's|^#baseurl=http://mirror.centos.org/$contentdir|baseurl=https://mirrors.ustc.edu.cn/centos|g' \
             -i.bak \
             /etc/yum.repos.d/CentOS-Stream-AppStream.repo \
             /etc/yum.repos.d/CentOS-Stream-BaseOS.repo \
             /etc/yum.repos.d/CentOS-Stream-Extras.repo \
             /etc/yum.repos.d/CentOS-Stream-PowerTools.repo

对于 CentOS 7，使用以下命令替换默认配置

    sudo sed -e 's|^mirrorlist=|#mirrorlist=|g' \
             -e 's|^#baseurl=http://mirror.centos.org/centos|baseurl=https://mirrors.ustc.edu.cn/centos|g' \
             -i.bak \
             /etc/yum.repos.d/CentOS-Base.repo

以上命令只替换了默认启用的仓库。替换之后请运行 `yum makecache`
更新缓存。

以下是替换之后的文件：

:::: warning
::: title
Warning
:::

以下给出的 `CentOS-Stream-PowerTools.repo`
设置了默认为停用状态。如需启用，请将 `enabled=0` 改为 `enabled=1`。
::::

-   CentOS 8 Stream：

    `/etc/yum.repos.d/CentOS-Stream-BaseOS.repo`{.interpreted-text
    role="file"} 文件：

    ::: literalinclude
    includes/centos8stream/CentOS-Stream-BaseOS.repo
    :::

    `/etc/yum.repos.d/CentOS-Stream-Extras.repo`{.interpreted-text
    role="file"} 文件：

    ::: literalinclude
    includes/centos8stream/CentOS-Stream-Extras.repo
    :::

    `/etc/yum.repos.d/CentOS-Stream-AppStream.repo`{.interpreted-text
    role="file"} 文件：

    ::: literalinclude
    includes/centos8stream/CentOS-Stream-AppStream.repo
    :::

    `/etc/yum.repos.d/CentOS-Stream-PowerTools.repo`{.interpreted-text
    role="file"} 文件：

    ::: literalinclude
    includes/centos8stream/CentOS-Stream-PowerTools.repo
    :::

-   CentOS 7：

    `/etc/yum.repos.d/CentOS-Base.repo`{.interpreted-text role="file"}
    文件：

    ::: literalinclude
    includes/centos7/CentOS-Base.repo
    :::

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
