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

以下是 Ubuntu 22.04.1 /etc/apt/sources.list 文件的参考配置内容：

::

    ## Note, this file is written by cloud-init on first boot of an instance
    ## modifications made here will not survive a re-bundle.
    ## if you wish to make changes you can:
    ## a.) add 'apt_preserve_sources_list: true' to /etc/cloud/cloud.cfg
    ##     or do the same in user-data
    ## b.) add sources in /etc/apt/sources.list.d
    ## c.) make changes to template file /etc/cloud/templates/sources.list.tmpl

    # See http://help.ubuntu.com/community/UpgradeNotes for how to upgrade to
    # newer versions of the distribution.
    deb http://mirrors.ustc.edu.cn/ubuntu-ports jammy main restricted
    # deb-src http://mirrors.ustc.edu.cn/ubuntu-ports jammy main restricted

    ## Major bug fix updates produced after the final release of the
    ## distribution.
    deb http://mirrors.ustc.edu.cn/ubuntu-ports jammy-updates main restricted
    # deb-src http://mirrors.ustc.edu.cn/ubuntu-ports jammy-updates main restricted

    ## N.B. software from this repository is ENTIRELY UNSUPPORTED by the Ubuntu
    ## team. Also, please note that software in universe WILL NOT receive any
    ## review or updates from the Ubuntu security team.
    deb http://mirrors.ustc.edu.cn/ubuntu-ports jammy universe
    # deb-src http://mirrors.ustc.edu.cn/ubuntu-ports jammy universe
    deb http://mirrors.ustc.edu.cn/ubuntu-ports jammy-updates universe
    # deb-src http://mirrors.ustc.edu.cn/ubuntu-ports jammy-updates universe

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
