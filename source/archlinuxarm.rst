=========================
Arch Linux ARM 源使用帮助
=========================

地址
====

https://mirrors.ustc.edu.cn/archlinuxarm/

说明
====

Arch Linux ARM 软件源

收录架构
========

ARMv5, ARMv6, ARMv7, AArch64

使用说明
========

编辑 :file:`/etc/pacman.d/mirrorlist` ，在文件的最顶端添加

::

    Server = https://mirrors.ustc.edu.cn/archlinuxarm/$arch/$repo

可以使用如下命令添加：

::

    # 修改前备份一下 /etc/pacman.d/mirrorlist 文件

    test -f /etc/pacman.d/mirrorlist.save || cp -f /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.save

    # 执行添加

    sed -i '1 i  Server = https://mirrors.ustc.edu.cn/archlinuxarm/$arch/$repo' /etc/pacman.d/mirrorlist


更新软件包缓存：
================

::

    pacman -Syy

相关链接
========

:官方主页: https://www.archlinuxarm.org/
:论坛: https://archlinuxarm.org/forum/
:Wiki: https://archlinuxarm.org/wiki
