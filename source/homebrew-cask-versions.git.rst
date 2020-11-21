=================================
Homebrew Cask Versions 源使用帮助
=================================

地址
====

https://mirrors.ustc.edu.cn/homebrew-cask-versions.git/

说明
====

Homebrew cask 其他版本 (alternative versions) 软件仓库，提供使用人数多的、需要的版本不在 cask 仓库中的应用。

使用说明
========

替换为 USTC 镜像：

::

    cd "$(brew --repo)"/Library/Taps/homebrew/homebrew-cask-versions
    git remote set-url origin https://mirrors.ustc.edu.cn/homebrew-cask-versions.git

重置为官方地址：

::

    cd "$(brew --repo)"/Library/Taps/homebrew/homebrew-cask-versions
    git remote set-url origin https://github.com/Homebrew/homebrew-cask-versions.git


相关镜像
========
- :doc:`brew.git`
- :doc:`homebrew-bottles`
- :doc:`homebrew-core.git`
- :doc:`homebrew-cask.git`
- :doc:`linuxbrew-core.git`
- :doc:`linuxbrew-bottles`

相关链接
========

:官方主页: https://github.com/Homebrew/homebrew-cask-versions
:Homebrew: https://brew.sh/
