=====================================
archive.raspberrypi.org 源使用帮助
=====================================

地址
====

http://mirrors.ustc.edu.cn/archive.raspberrypi.org/debian/

说明
====

树莓派的 archive.raspberrypi.org 软件源，也即 :file:`/etc/apt/sources.list.d/raspi.list` ，

是由树莓派基金会提供的软件源，包括 ui 相关程序 ( 如 Raspbian 的桌面环境 PIXEL DE) 及部分由树莓派基金会为树莓派编写的软件，通常与 archive.raspbian.org ( 参考 :doc:`raspbian` ) 一起使用

收录架构
========

* armhf
* x86
* x86_64

收录版本
========

* wheezy
* jessie
* stretch

当前 Stable 为 Debian 9，代号为 Stretch

使用说明
========

.. warning::
    操作前请做好相应备份

一般情况下，将 :file:`/etc/apt/sources.list.d/raspi.list` 文件中 Debian 默认的源地址 ``http://archive.raspberrypi.org/``
替换为 ``http://mirrors.ustc.edu.cn/archive.raspberrypi.org/`` 即可。

可以使用如下命令：

::

  sudo sed -i 's|archive.raspberrypi.org|mirrors.ustc.edu.cn/archive.raspberrypi.org|g' /etc/apt/sources.list.d/raspi.list

当然也可以直接编辑 :file:`/etc/apt/sources.list.d/raspi.list` 文件（需要使用 sudo）。以下是 Debian Stable 参考配置内容：

::

    deb http://mirrors.ustc.edu.cn/archive.raspberrypi.org/debian/ stretch main ui
    #deb-src http://mirrors.ustc.edu.cn/archive.raspberrypi.org/debian/ stretch main ui

更改完 :file:`raspi.list` 文件后请运行 ``sudo apt-get update`` 更新索引以生效。

.. tip::
    使用 HTTPS 可以有效避免国内运营商的缓存劫持，但需要事先安装 ``apt-transport-https``。

相关链接
========

:官方主页: https://www.raspberrypi.org/
:文档: https://www.raspberrypi.org/documentation/
