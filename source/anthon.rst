==================
AOSC OS 源使用帮助
==================

地址
====

https://mirrors.nju.edu.cn/anthon

说明
====

AOSC OS（安同 OS）软件源

收录架构
========

AOSC OS 支持的所有架构，包括：

* AMD64（x86_64）
* ARM

  * ARMv7（armel）
  * ARMv8（arm64, aarch64）

* MIPS

  * mipsel
  * mips64el

* PowerPC

  * powerpc（ppc32）
  * ppc64

使用说明
========

AOSC OS 内置 ``apt-gen-list`` 工具来开关镜像源。要使用 NJU 源，执行：

::

  sudo apt-gen-list -e 10-nju

注意目前这将关闭其它镜像源。详细用法请执行 ``apt-gen-list -h`` 获取。

当然，也可以直接编辑 :file:`/etc/apt/sources.list` 文件。对于任一架构 ``${ARCH}``，需要在 :file:`/etc/apt/sources.list` 中同时写入：

::

  deb https://mirrors.nju.edu.cn/anthon/os-${ARCH}/os3-dpkg/ /
  deb https://mirrors.nju.edu.cn/anthon/os-noarch/os3-dpkg/ /

其中 ``${ARCH}`` 可以是：

* ``amd64`` （x86_64）
* ``armel`` （ARMv7）
* ``arm64`` （ARMv8）
* ``mipsel``
* ``mips64el``
* ``powerpc``
* ``ppc64``

执行完上面任一步骤后，请运行 ``sudo apt-get update`` 更新索引以生效。

相关链接
========

:官方主页: https://aosc.io
:文档: https://github.com/AOSC-Dev/aosc-os/wiki
:镜像列表: https://aosc.io/about
