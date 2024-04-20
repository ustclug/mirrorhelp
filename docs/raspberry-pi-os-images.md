# Raspberry Pi OS Images

## 地址

<http://mirrors.ustc.edu.cn/raspberry-pi-os-images/>

## 说明

目前仅同步了包括 raspios 在内的几个常用版本，以及部分工具等。

raspios 的默认用户是 pi，密码是 raspberry，root 默认关闭。

## 系统架构

-   armhf
-   arm64 (Beta)
-   x86

## 收录版本

最新的稳定版（bullseye）

## 使用说明

目前本镜像包含如下内容：

-   imager: Raspberry Pi Imager 官方刻录器。
-   raspios_arm64: Arm64 架构的 Raspberry Pi OS（Beta）
-   raspios_armhf: Armhf 架构的 Raspberry Pi OS
-   raspios_full_armhf: Armhf 架构的 Raspberry Pi
    OS，并包含官方推荐的软件
-   raspios_lite_arm64: Arm64 架构的 Raspberry Pi OS（Beta，不含桌面）
-   raspios_lite_armhf: Armhf 架构的 Raspberry Pi OS（不含桌面）
-   rpd_x86: Raspberry Pi Desktop，用于 x86 架构的设备
-   Raspberry_Pi_Education_Manual.pdf: 教学用树莓派帮助手册

需要安装 Raspberry Pi OS 时，一般下载 images 目录中的最新的即可，比如
arm64 的树莓派下载
<https://mirrors.ustc.edu.cn/raspberry-pi-os-images/raspios_lite_arm64/images/>
中最新的 zip 压缩包即可， 解压完 zip 压缩包后即可开始刻录。
