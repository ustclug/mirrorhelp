======================
Debian 源使用帮助
======================

地址
====

https://mirrors.ustc.edu.cn/debian/

说明
====

Debian 软件源

收录架构
========

Debian 支持的所有架构，如 AMD64 (x86_64), Intel x86, ARM, MIPS, ppc64el, s390x 等


收录版本
========

Debian Old Stable, Stable, Testing, Unstable(sid)

当前 Stable 为 Debian 12，代号为 Bookworm

使用说明
========


.. warning::
    操作前请做好相应备份

一般情况下，将 :file:`/etc/apt/sources.list` 文件中 Debian 默认的源地址 ``http://deb.debian.org/``
替换为 ``http://mirrors.ustc.edu.cn`` 即可。

可以使用如下命令：

::

  sudo sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list

当然也可以直接编辑 :file:`/etc/apt/sources.list` 文件（需要使用 sudo）。以下是 Debian Stable 参考配置内容：

::

    deb http://mirrors.ustc.edu.cn/debian stable main contrib non-free non-free-firmware
    # deb-src http://mirrors.ustc.edu.cn/debian stable main contrib non-free non-free-firmware
    deb http://mirrors.ustc.edu.cn/debian stable-updates main contrib non-free non-free-firmware
    # deb-src http://mirrors.ustc.edu.cn/debian stable-updates main contrib non-free non-free-firmware

    # deb http://mirrors.ustc.edu.cn/debian stable-proposed-updates main contrib non-free non-free-firmware
    # deb-src http://mirrors.ustc.edu.cn/debian stable-proposed-updates main contrib non-free non-free-firmware

.. tip::
    从 Debian 12 (bookworm) 开始，仓库添加了非自由固件组件 ``non-free-firmware``。
    如果正在使用 bookworm, testing 或 sid，并且需要使用非自由固件，则在编辑配置时需要添加 ``non-free-firmware``。
    其中以上参考配置已经添加。
    详情参考 https://wiki.debian.org/Firmware 与 `Debian bug #1030189 <https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1030189>`_。

.. tip::
    Debian 12 (bookworm) 的\ **容器**\ 镜像开始使用 DEB822 格式，而非上文使用的传统的 One-Line-Style 格式。
    对应需要修改的文件为 :file:`/etc/apt/sources.list.d/debian.sources`。同样可以使用如下命令：

    ::

        sudo sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list.d/debian.sources
    
    以下是在 Debian 12 容器镜像中\ **同时修改了 Debian 与 Debian Security 源的情况下**\ 的参考配置内容：

    ::

        Types: deb
        URIs: http://mirrors.ustc.edu.cn/debian
        Suites: bookworm bookworm-updates
        Components: main
        Signed-By: /usr/share/keyrings/debian-archive-keyring.gpg

        Types: deb
        URIs: http://mirrors.ustc.edu.cn/debian-security
        Suites: bookworm-security
        Components: main
        Signed-By: /usr/share/keyrings/debian-archive-keyring.gpg

同时你也可能需要更改 Debian Security 源，请参考 :doc:`debian-security`。

更改完 :file:`sources.list` 文件后请运行 ``sudo apt-get update`` 更新索引以生效。

.. tip::
    使用 HTTPS 可以有效避免国内运营商的缓存劫持，但需要事先安装 ``apt-transport-https`` (Debian Buster
    及以上版本不需要)。

另外，也可以使用 snullp 大叔开发的 `配置生成器 <https://mirrors.ustc.edu.cn/repogen>`_ 。

.. warning::
    在 apt 2.1.9 及以后的版本中，apt 的 HTTP Pipelining 特性与 Nginx 服务器疑似存在一定的不兼容问题，可能导致高带宽从镜像站下载大量软件包
    （例如系统升级）时出现偶发的 Connection reset by peer 错误
    （详见 `Debian bug #973581 <https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=973581>`_）。

    目前，用户可以通过关闭 HTTP Pipelining 特性解决此问题。
    如果需要关闭，可以在使用 ``apt`` 命令时加上 ``-o Acquire::http::Pipeline-Depth=0`` 参数，
    或使用以下命令将相关设置加入 apt 系统配置中：

    ::

        echo "Acquire::http::Pipeline-Depth \"0\";" > /etc/apt/apt.conf.d/99nopipelining

相关链接
========

:官方主页: https://www.debian.org/
:邮件列表: https://www.debian.org/MailingLists/
:Wiki: https://wiki.debian.org/
:文档: https://www.debian.org/doc/
:镜像列表: https://www.debian.org/mirror/list
