========================
Kali Linux 源使用帮助
========================

地址
====

https://mirrors.nju.edu.cn/kali/

说明
====

Kali Linux 软件源

支持的系统架构
==============

amd64, armel, armhf, i386

使用说明
========

编辑 :file:`/etc/apt/sources.list` 文件, 在文件最前面添加以下条目：

::

  deb https://mirrors.nju.edu.cn/kali kali-rolling main non-free contrib
  deb-src https://mirrors.nju.edu.cn/kali kali-rolling main non-free contrib
  
更改完 :file:`sources.list` 文件后请运行 ``sudo apt-get update`` 更新索引以生效。

相关链接
========

:Kali Linux 主页: https://www.kali.org/
:论坛: http://forums.kali.org/
:文档: https://www.kali.org/kali-linux-documentation/
