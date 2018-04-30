===================
MSYS2 源使用帮助
===================

地址
====

https://mirrors.ustc.edu.cn/msys2/

说明
====

MSYS2镜像

收录架构
========

*   MINGW: i686, x86_64
*   MSYS: i686, x86_64

获取基本组件包
==============

访问该镜像目录下的 ``distrib/`` 目录 (`x86_64 <http://mirrors.ustc.edu.cn/msys2/distrib/x86_64/>`_ 、 `i686 <http://mirrors.ustc.edu.cn/msys2/distrib/i686/>`_ )，找到名为 ``msys2-<架构>-<日期>.exe`` 的文件 （如 ``msys2-x86_64-20141113.exe`` ），下载安装即可。

pacman的配置
============

编辑 :file:`/etc/pacman.d/mirrorlist.mingw32` ，在文件开头添加：

::
    
    Server = http://mirrors.ustc.edu.cn/msys2/mingw/i686   


编辑 :file:`/etc/pacman.d/mirrorlist.mingw64` ，在文件开头添加

::

    Server = http://mirrors.ustc.edu.cn/msys2/mingw/x86_64

编辑 :file:`/etc/pacman.d/mirrorlist.msys` ，在文件开头添加

::

    Server = http://mirrors.ustc.edu.cn/msys2/msys/$arch

然后执行 ``pacman -Sy`` 刷新软件包数据即可。

相关链接
========

:MSYS2主页: https://www.msys2.org/
