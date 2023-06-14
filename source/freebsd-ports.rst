========================
FreeBSD ports 源使用帮助
========================

地址
====

http://mirrors.ustc.edu.cn/freebsd-ports/

说明
====

FreeBSD ports 软件源

使用方法
========

在 :file:`/etc/make.conf` 中添加以下内容（如果文件不存在，则新建之）：

::

    MASTER_SITE_OVERRIDE?=http://mirrors.ustc.edu.cn/freebsd-ports/distfiles/${DIST_SUBDIR}/

ports.tar.gz 文件为 Ports Collection，可以下载后解压到 ``/usr/ports/`` 目录。
也可参考 FreeBSD Handbook 中 `Installing the Ports Collection`_ 一节，使用 ``git`` 获取 ports tree：

::

    # git clone --depth 1 https://mirrors.ustc.edu.cn/freebsd-ports/ports.git /usr/ports

.. attention::
    部分 ports 的源代码需要从 http://distcache.freebsd.org/ports-distfiles/ 以外的 master site 下载，本镜像不包含这些文件。

.. attention::
    本镜像仅包含 ports tree 中 HEAD branch 引用到的文件。季度分支（如 ``2020Q4``）引用的文件有可能不包含在本镜像中。

相关链接
========

:官方主页: https://www.freebsd.org
:论坛: https://forums.freebsd.org
:文档: https://www.freebsd.org/doc
:官方介绍: https://www.freebsd.org/ports

.. _Installing the Ports Collection: https://docs.freebsd.org/en/books/handbook/ports/#ports-using-installation-methods
