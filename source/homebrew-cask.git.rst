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

使用 USTC 镜像安装，或将已安装的仓库远程替换为 USTC 镜像：

::

    brew tap --custom-remote --force-auto-update homebrew/cask https://mirrors.ustc.edu.cn/homebrew-cask.git

重置为官方地址：

::

    brew tap --custom-remote --force-auto-update homebrew/cask https://github.com/Homebrew/homebrew-cask

.. note::
    Caskroom 的 Git 地址在 2018 年 5 月 25 日从 https://github.com/caskroom/homebrew-cask 迁移到了
    https://github.com/Homebrew/homebrew-cask 。

相关镜像
========
- :doc:`brew.git`
- :doc:`homebrew-bottles`
- :doc:`homebrew-core.git`
- :doc:`homebrew-cask-versions.git`
- :doc:`linuxbrew-core.git`
- :doc:`linuxbrew-bottles`

相关链接
========

:官方主页: https://caskroom.github.io
:Homebrew: https://brew.sh/
