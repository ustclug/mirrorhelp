===================
Termux 源使用帮助
===================

地址
====

https://mirrors.ustc.edu.cn/termux

说明
====

Termux APT 源镜像

收录架构
========

*   ARM, AArch64, i686, x86_64

使用说明
==============

用文本编辑器（如 ``vim`` ）打开 :file:`/data/data/com.termux/files/usr/etc/apt/sources.list`，将 ``https://termux.net`` 替换成 ``https://mirrors.ustc.edu.cn/termux``，保存退出即可。

你也可以使用 ``sed`` 命令进行文本替换：

::

    sed -i 's,https://termux.net,https://mirrors.ustc.edu.cn/termux,' $PREFIX/etc/apt/sources.list

注：Termux 会自动将环境变量 ``$PREFIX`` 设定为 :file:`/data/data/com.termux/files/usr`

相关链接
========

:Termux 官网: https://termux.com/
:Google Play: https://play.google.com/store/apps/details?id=com.termux
