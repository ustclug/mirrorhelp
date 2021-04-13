===========================
Homebrew Bottles 源使用帮助
===========================

地址
====

https://mirrors.ustc.edu.cn/homebrew-bottles/bottles/

说明
====

Homebrew 预编译二进制软件包

收录仓库
========

* homebrew/homebrew-core

使用说明
========

请在运行 brew 前设置环境变量 ``HOMEBREW_BOTTLE_DOMAIN`` ，值为 ``https://mirrors.ustc.edu.cn/homebrew-bottles/bottles`` 。

对于 bash 用户：

::

    echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles/bottles' >> ~/.bash_profile
    source ~/.bash_profile

对于 zsh 用户：

::

    echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles/bottles' >> ~/.zshrc
    source ~/.zshrc

相关镜像
========
- :doc:`brew.git`
- :doc:`homebrew-core.git`
- :doc:`homebrew-cask.git`
- :doc:`homebrew-cask-versions.git`
- :doc:`linuxbrew-core.git`
- :doc:`linuxbrew-bottles`

相关链接
========

:官方主页: http://brew.sh/
:Bottles 介绍: http://docs.brew.sh/Bottles.html
