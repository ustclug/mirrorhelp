=========================
Linuxbrew Core 源使用帮助
=========================

地址
====

https://mirrors.ustc.edu.cn/linuxbrew-core.git/

说明
====

Linuxbrew 核心软件仓库

使用说明
========

替换 USTC 镜像：

::

    cd "$(brew --repo homebrew/core)"
    git remote set-url origin https://mirrors.ustc.edu.cn/linuxbrew-core.git

重置为官方地址：

::

    cd "$(brew --repo homebrew/core)"
    git remote set-url origin https://github.com/Homebrew/linuxbrew-core

相关镜像
========
- :doc:`homebrew-bottles`
- :doc:`homebrew-core.git`
- :doc:`homebrew-cask.git`
- :doc:`homebrew-cask-versions.git`
- :doc:`linuxbrew-bottles`

相关链接
========

:官方主页: https://brew.sh/
:Linuxbrew 文档: https://docs.brew.sh/Homebrew-on-Linux
