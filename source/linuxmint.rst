========================
Linux Mint 源使用帮助
========================

地址
====

https://mirrors.ustc.edu.cn/linuxmint/

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
 
1. 打开 Software Manager（软件管理器） ，点击 Edit（编辑），选择 Software Sources（软件源）。
 
2. 在 Main（主要）中选择 http://mirrors.ustc.edu.cn/linuxmint；如果你在使用 Linux Mint，在 Base（基础）中选择 http://mirrors.ustc.edu.cn/ubuntu，如果你在使用 LMDE，选择 http://debian.ustc.edu.cn/debian。
 
3. 编辑 :file:`/etc/apt/sources.list.d/official-lackage-repositories.list` ：

::

 sudo xed /etc/apt/sources.list.d/official-lackage-repositories.list
 
* 如果你在使用 Linux Mint，将 security 源换为中科大的源，以 Linux Mint 18.x 为例：

::

 deb http://mirrors.ustc.edu.cn/ubuntu/ xenial-security main restricted universe multiverse
 
* 如果你在使用 LMDE，将 security 源和 deb-multimedia 源换为中科大的源，以 LMDE 2 为例：

::

 deb http://mirrors.ustc.edu.cn/debian-security/ jessie/updates main non-free contrib
 deb http://mirrors.ustc.edu.cn/deb-multimedia/ jessie main non-free
 
* 保存退出。
 
4. 最后运行 ``sudo apt-get update`` 更新索引以生效。 

相关链接
========

:官方主页: https://www.linuxmint.com/
:论坛: https://forums.linuxmint.com/index.php
:文档: https://linuxmint.com/documentation.php
