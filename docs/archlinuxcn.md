# Arch Linux CN

## 地址

<https://mirrors.ustc.edu.cn/archlinuxcn/>

## 说明

Arch Linux CN 软件源

## 简介

Arch Linux 中文社区仓库是由 Arch Linux
中文社区驱动的非官方用户仓库。包含中文用户常用软件、工具、字体/美化包等。

仓库地址：<http://repo.archlinuxcn.org>

## 使用说明

在 `/etc/pacman.conf` 文件末尾添加两行：

    [archlinuxcn]
    Server = https://mirrors.ustc.edu.cn/archlinuxcn/$arch

然后请安装 `archlinuxcn-keyring` 包以导入 GPG key。

!!! warning

    2023 年 12 月后，在新系统下安装 `archlinuxcn-keyring` 时可能会出现错误：

        error: archlinuxcn-keyring: Signature from "Jiachen YANG (Arch Linux Packager Signing Key) " is marginal trust

    需要在本地信任 farseerfc 的 GPG key：

        sudo pacman-key --lsign-key "farseerfc@archlinux.org"

    然后重试安装。详情参见
    [新系统中安装 archlinuxcn-keyring 包前需要手动信任 farseerfc 的 key](https://www.archlinuxcn.org/archlinuxcn-keyring-manually-trust-farseerfc-key/)。

## 相关链接

Arch Linux 中文社区主页

:   <https://www.archlinuxcn.org>

Arch Linux 中文社区仓库 / 镜像加速源介绍

:   <https://www.archlinuxcn.org/archlinux-cn-repo-and-mirror/>
