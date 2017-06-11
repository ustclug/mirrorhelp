============================
Debian Multimedia 源使用帮助
============================

地址
====

https://mirrors.ustc.edu.cn/debian-multimedia/

说明
====

Debian 第三方多媒体软件源

收录架构
========

Debian Multimedia 支持的所有架构，如 AMD64 (x86_64), Intel x86, ARM, MIPS 等


收录版本
========

Debian Old Stable, Stable, Testing, Unstable(sid)

当前 Stable 为 Debian 8，代号为 Jessie

使用说明
========

.. important::
    该 Debian Multimedia 不是官方 Debian 项目，是为 deb-multimedia.org 的镜像，两者区别
    见 https://wiki.debian.org/DebianMultimedia/FAQ

以 Jessie 为例，在 :file:`/etc/apt/sources.list` 中加入

::

    deb http://mirrors.ustc.edu.cn/debian-multimedia/ jessie main non-free
    # deb-src http://mirrors.ustc.edu.cn/debian-multimedia/ jessie main non-free
    deb http://mirrors.ustc.edu.cn/debian-multimedia/ jessie-backports main
    # deb-src http://mirrors.ustc.edu.cn/debian-multimedia/ jessie-backports main

更改完 :file:`sources.list` 文件后请导入deb-multimedia-keyring

::

    wget https://mirrors.ustc.edu.cn/deb-multimedia/pool/main/d/deb-multimedia-keyring/deb-multimedia-keyring_2016.8.1_all.deb
    sudo dpkg -i deb-multimedia-keyring_2016.8.1_all.deb
    
然后请运行 ``sudo apt-get update`` 更新索引以生效。

.. tip::
    使用 HTTPS 可以有效避免国内运营商的缓存劫持，但需要事先安装 ``apt-transport-https``

相关链接
========

:官方主页: https://deb-multimedia.org/
:邮件列表: https://deb-multimedia.org/mailinglist
:镜像列表: https://deb-multimedia.org/debian-m
