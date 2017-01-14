========================
Homebrew Core 源使用帮助
========================

地址
====

https://mirrors.ustc.edu.cn/homebrew-core.git/

说明
====

Homebrew 核心软件仓库

使用说明
========

替换 USTC 镜像：

::

    cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
    git remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git

重置为官方地址：

::

    cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
    git remote set-url origin https://github.com/Homebrew/homebrew-core.git

相关镜像
========
- :doc:`brew.git`
- :doc:`homebrew-bottles`

相关链接
========

:官方主页: http://brew.sh/
:brew 帮助手册: http://docs.brew.sh/brew.1.html
