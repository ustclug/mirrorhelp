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

Termux 目前（2021 年 6 月）的官方源为 packages.termux.org，我们推荐先更新 ``termux-tools`` 软件包，然后直接使用 ``termux-change-repo`` 命令选择 Mirrors by USTC 即可。

如果想要手动更换 Termux APT 源的话，可以编辑 :file:`/data/data/com.termux/files/usr/etc/apt/sources.list` 为如下内容

::

    deb https://mirrors.ustc.edu.cn/termux/apt/termux-main stable main

或者，你也可以使用 ``sed`` 命令进行文本替换：

::

    sed -i 's@packages.termux.org@mirrors.ustc.edu.cn/termux@' $PREFIX/etc/apt/sources.list
    pkg up

注：Termux 会自动将环境变量 ``$PREFIX`` 设定为 :file:`/data/data/com.termux/files/usr`

.. warning::
    Google Play 上的 Termux 已被弃用，如安装会产生兼容性问题。请通过 GitHub 或 F-Droid 来安装 Termux。

相关链接
========

:Termux 官网: https://termux.com/
:GitHub: https://github.com/termux/termux-app
:F-Droid: https://f-droid.org/zh_Hant/packages/com.termux
