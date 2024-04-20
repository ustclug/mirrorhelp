# Ubuntu Ports 源使用帮助

## 地址

<https://mirrors.ustc.edu.cn/ubuntu-ports/>

## 说明

Ubuntu 软件源

## 收录架构

arm64, armhf, PowerPC, ppc64el, s390x

## 收录版本

所有 Ubuntu 当前对该架构支持的版本，包括开发版

对于 Ubuntu 不再支持的版本，请参考
`ubuntu-old-releases`{.interpreted-text role="doc"}

## 使用说明

### 手动更改配置文件

:::: warning
::: title
Warning
:::

操作前请做好相应备份
::::

在 `/etc/apt/sources.list`{.interpreted-text role="file"}
文件中，将软件源的地址改为 `http://mirrors.ustc.edu.cn/ubuntu-ports`

以下是 Ubuntu 22.04 /etc/apt/sources.list 文件的参考配置内容：

    # 默认注释了源码仓库，如有需要可自行取消注释
    deb https://mirrors.ustc.edu.cn/ubuntu-ports/ jammy main restricted universe multiverse
    # deb-src https://mirrors.ustc.edu.cn/ubuntu-ports/ jammy main main restricted universe multiverse
    deb https://mirrors.ustc.edu.cn/ubuntu-ports/ jammy-updates main restricted universe multiverse
    # deb-src https://mirrors.ustc.edu.cn/ubuntu-ports/ jammy-updates main restricted universe multiverse
    deb https://mirrors.ustc.edu.cn/ubuntu-ports/ jammy-backports main restricted universe multiverse
    # deb-src https://mirrors.ustc.edu.cn/ubuntu-ports/ jammy-backports main restricted universe multiverse
    deb https://mirrors.ustc.edu.cn/ubuntu-ports/ jammy-security main restricted universe multiverse
    # deb-src https://mirrors.ustc.edu.cn/ubuntu-ports/ jammy-security main restricted universe multiverse

    # 预发布软件源，不建议启用
    # deb https://mirrors.ustc.edu.cn/ubuntu-ports/ jammy-proposed main restricted universe multiverse
    # deb-src https://mirrors.ustc.edu.cn/ubuntu-ports/ jammy-proposed main restricted universe multiverse

更改完 `sources.list`{.interpreted-text role="file"} 文件后请运行
`sudo apt-get update` 更新索引以生效。

:::: tip
::: title
Tip
:::

使用 HTTPS 可以有效避免国内运营商的缓存劫持，但需要事先安装
`apt-transport-https`
::::

### 镜像下载

相关架构的 ISO 下载请参考 `ubuntu-cdimage`{.interpreted-text role="doc"}

## 相关链接

Ubuntu ARM

:   <https://wiki.ubuntu.com/ARM>

Ubuntu PowerPC

:   <https://wiki.ubuntu.com/PowerPC>

Ubuntu ppc64el

:   <https://wiki.ubuntu.com/ppc64el>

Ubuntu s390x

:   <https://wiki.ubuntu.com/S390X>
