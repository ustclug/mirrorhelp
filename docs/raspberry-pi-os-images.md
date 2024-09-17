# Raspberry Pi OS Images

## 地址

<https://mirrors.ustc.edu.cn/raspberry-pi-os-images/>

## 说明

目前仅同步了包括 raspios 在内的几个常用版本，以及部分工具等。

raspios 的默认用户是 `pi`，密码是 `raspberry`，root 默认关闭。

## 系统架构

- armhf
- arm64
- x86

## 收录版本

- bullseye
- bookworm

## 使用说明

目前本镜像包含如下内容：

imager

:   Raspberry Pi Imager 官方刻录器。

raspios_(arm64, armhf)

:   Raspberry Pi OS（含桌面）

raspios_full_(arm64, armhf)

:   Raspberry Pi OS（含桌面，并包含官方推荐的软件）

raspios_lite_(arm64, armhf)

:   Raspberry Pi OS（不含桌面）

rpd_x86

:   Raspberry Pi Desktop，用于 x86 架构的设备

Raspberry_Pi_Education_Manual.pdf

:   教学用树莓派帮助手册

需要安装 Raspberry Pi OS 时，一般下载 images 目录中的最新的即可，比如 arm64 的树莓派下载 <https://mirrors.ustc.edu.cn/raspberry-pi-os-images/raspios_lite_arm64/images/> 中最新的 zip 压缩包即可，解压完 zip 压缩包后即可开始刻录。

!!! note

    对于刚接触 Linux 的同学，使用 `imager` 也许会是个节省时间的好办法。

    关于使用 armhf (32 bit) 还是 arm64 (64 bit) 版本，可以参考 [Raspberry Pi OS (64-bit)](https://www.raspberrypi.com/news/raspberry-pi-os-64-bit/)。tl;dr:

    - 无特殊兼容需求的情况下，推荐使用 arm64
    - 对于 4GB 及以上内存的设备，推荐使用 arm64
    - 对于古早设备 (Rpi 1, 2, Zero), 请使用 armhf

## 相关链接

- 树莓派链接

    官方主页

    :   <https://www.raspberrypi.org/>

    文档

    :   <https://www.raspberrypi.org/documentation/>

- 其他镜像帮助

    - [Raspbian 镜像使用帮助](raspbian.md)
    - [Raspberrypi 镜像使用帮助](raspberrypi.md)
