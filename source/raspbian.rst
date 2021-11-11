===================
Raspbian 源使用帮助
===================

地址
====

https://mirrors.ustc.edu.cn/raspbian/

说明
====

Raspbian 软件源

系统架构
========

armhf

收录版本
========

* stretch (oldoldstable)
* buster (oldstable)
* bullseye (stable)
* bookworm (testing)

使用说明
========

.. warning::
    操作前请做好相应备份

将 :file:`/etc/apt/sources.list` 文件中默认的源地址 ``http://raspbian.raspberrypi.org/`` 替换为 ``http://mirrors.ustc.edu.cn/raspbian/`` 即可。

raspbian 2018-04-19 之后的镜像默认源已经更改，用如下命令替换：

::

  sudo sed -i 's|raspbian.raspberrypi.org|mirrors.ustc.edu.cn/raspbian|g' /etc/apt/sources.list

旧版的系统可以用以下命令替换：

::

  sudo sed -i 's|mirrordirector.raspbian.org|mirrors.ustc.edu.cn/raspbian|g' /etc/apt/sources.list
  sudo sed -i 's|archive.raspbian.org|mirrors.ustc.edu.cn/raspbian|g' /etc/apt/sources.list


当然也可以直接编辑 :file:`/etc/apt/sources.list` 文件（需要使用 sudo）。删除原文件所有内容，用以下内容取代（以 Bullseye 示例）：

::

    deb http://mirrors.ustc.edu.cn/raspbian/raspbian/ bullseye main contrib non-free rpi
    # deb-src http://mirrors.ustc.edu.cn/raspbian/raspbian/ bullseye main contrib non-free rpi

Arm64 架构的 Raspberry Pi OS 仍处于 beta 状态，本镜像上游亦不含此架构。对于 arm64 的 Raspberry Pi OS，可以直接使用 arm64 Debian 的源（以 Bullseye 示例）：

::

    deb https://mirrors.ustc.edu.cn/debian/ bullseye main contrib non-free
    # deb-src http://mirrors.ustc.edu.cn/debian bullseye main contrib non-free
    deb https://mirrors.ustc.edu.cn/debian/ bullseye-updates main contrib non-free
    # deb-src http://mirrors.ustc.edu.cn/debian bullseye-updates main contrib non-free
    deb https://mirrors.ustc.edu.cn/debian-security bullseye-security main contrib non-free
    # deb-src http://mirrors.ustc.edu.cn/debian-security/ bullseye-security main non-free contrib

编辑此文件后，请使用 ``sudo apt-get update`` 命令，更新软件索引。

同时也可能需要更改 archive.raspberrypi.org 源，请参考 :doc:`raspberrypi` 。

相关链接
========

Raspbian 链接
  :Raspbian 主页: http://www.raspbian.org/
  :文档: http://www.raspbian.org/RaspbianDocumentation
  :Bug Tracker: http://www.raspbian.org/RaspbianBugs
  :镜像列表: http://www.raspbian.org/RaspbianMirrors

树莓派链接
  :树莓派基金会主页: https://www.raspberrypi.org/
  :树莓派基金会论坛 Raspberry Pi OS 版块: https://www.raspberrypi.org/forums/viewforum.php?f=66
