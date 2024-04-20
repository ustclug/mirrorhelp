# AOSC OS

## 地址

<https://mirrors.ustc.edu.cn/anthon>

## 说明

AOSC OS（安同 OS）软件源。
AOSC OS 是一个由安同开源社区（<https://aosc.io>）开发的半滚动 Linux 发行版，支持多种处理器架构。

## 使用说明

AOSC OS 内置 `apt-gen-list` 工具来开关社区提供的可用镜像源。要启用 USTC 源，执行：

    sudo apt-gen-list add-mirror ustc

要仅启用 USTC 源，执行：

    sudo apt-gen-list set-mirror ustc

关于 `apt-gen-list` 的语义和详细用法，请执行 `apt-gen-list help` 查看帮助。

## 相关链接

官方主页

:   <https://aosc.io>

文档

:   <https://wiki.aosc.io>

镜像列表

:   <https://aosc.io/repo>
