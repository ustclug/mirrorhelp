========================
Linux Mint 源使用帮助
========================

地址
====

https://mirrors.nju.edu.cn/linuxmint/

说明
====

Linux Mint 软件源

收录架构
========

i386，amd64

收录版本
========

* 所有 Linux Mint 发行版本
* 所有 LMDE 发行版本

使用方法
========

.. warning::
	操作前请做好相应备份。 
 
编辑 :file:`/etc/apt/sources.list.d/official-lackage-repositories.list` ：

* 对于基于 Ubuntu 的原版，以 Linuxmint 18.2 为例：

::

	deb https://mirrors.nju.edu.cn/linuxmint/ sonya main upstream import backport 
	deb https://mirrors.nju.edu.cn/ubuntu/ xenial main restricted universe multiverse
	deb https://mirrors.nju.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse
	deb https://mirrors.nju.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
	deb https://mirrors.nju.edu.cn/ubuntu/ xenial-security main restricted universe multiverse
	deb http://archive.canonical.com/ubuntu/ xenial partner
	
* 对于基于 Debian 的 LMDE，以 LMDE 2 为例：

::

	deb https://mirrors.nju.edu.cn/linuxmint/ betsy main upstream import
	deb https://mirrors.nju.edu.cn/debian jessie main contrib non-free
	deb https://mirrors.nju.edu.cn/debian jessie-updates main contrib non-free
	deb https://mirrors.nju.edu.cn/debian jessie-backports main contrib non-free
	deb https://mirrors.nju.edu.cn/debian-security/ jessie/updates main non-free contrib
	deb https://mirrors.nju.edu.cn/deb-multimedia/ jessie main non-free

 
然后运行 ``sudo apt-get update`` 更新索引以生效。 

.. tip::
	完成后请不要再使用 mintsources（自带的图形化软件源设置工具）进行任何操作，因为在操作后，无论是否有按“确定”，mintsources 均会复写 :file:`/etc/apt/sources.list.d/official-lackage-repositories.list` 。

相关链接
========

:官方主页: https://www.linuxmint.com/
:论坛: https://forums.linuxmint.com/index.php
:文档: https://linuxmint.com/documentation.php
