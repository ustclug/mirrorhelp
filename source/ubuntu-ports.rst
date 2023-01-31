=======================
Ubuntu Ports 源使用帮助
=======================

地址
====

https://mirrors.ustc.edu.cn/ubuntu-ports/

说明
====

Ubuntu 软件源

收录架构
========

arm64, armhf, PowerPC, ppc64el, s390x

收录版本
========

所有 Ubuntu 当前对该架构支持的版本，包括开发版

对于 Ubuntu 不再支持的版本，请参考 :doc:`ubuntu-old-releases`

使用说明
========

手动更改配置文件
----------------

.. warning::
    操作前请做好相应备份

在 :file:`/etc/apt/sources.list` 文件中，将软件源的地址改为 ``http://mirrors.ustc.edu.cn/ubuntu-ports``

可以使用如下命令：

::

sudo sed -i 's@//ports.ubuntu.com@//mirrors.ustc.edu.cn@g' /etc/apt/sources.list

更改完 :file:`sources.list` 文件后请运行 ``sudo apt-get update`` 更新索引以生效。

.. tip::
    使用 HTTPS 可以有效避免国内运营商的缓存劫持，但需要事先安装 ``apt-transport-https``

镜像下载
--------

相关架构的 ISO 下载请参考 :doc:`ubuntu-cdimage`

相关链接
========

:Ubuntu ARM: https://wiki.ubuntu.com/ARM
:Ubuntu PowerPC: https://wiki.ubuntu.com/PowerPC
:Ubuntu ppc64el: https://wiki.ubuntu.com/ppc64el
:Ubuntu s390x: https://wiki.ubuntu.com/S390X
