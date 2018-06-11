========================
Homebrew Cask 源使用帮助
========================

地址
====

https://mirrors.ustc.edu.cn/homebrew-cask.git/

说明
====

Homebrew cask 软件仓库，提供 macOS 应用和大型二进制文件

使用说明
========

替换为 USTC 镜像：

::

    cd "$(brew --repo)"/Library/Taps/homebrew/homebrew-cask
    git remote set-url origin https://mirrors.ustc.edu.cn/homebrew-cask.git

重置为官方地址：

::

    cd "$(brew --repo)"/Library/Taps/homebrew/homebrew-cask
    git remote set-url origin https://github.com/caskroom/homebrew-cask

相关镜像
========
- :doc:`brew.git`
- :doc:`homebrew-bottles`
- :doc:`homebrew-core.git`

相关链接
========

:官方主页: https://caskroom.github.io
:Homrbew: http://brew.sh/
