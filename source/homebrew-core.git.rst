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

    export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.ustc.edu.cn/homebrew-core.git"
    brew update

.. note::
    若用户设置了环境变量 ``HOMEBREW_CORE_GIT_REMOTE``，则每次运行 ``brew update`` 时将会自动设置远程。
    推荐用户将环境变量 ``HOMEBREW_CORE_GIT_REMOTE`` 加入 shell 的 profile 设置中。

    ::

        # 对于 bash 用户
        echo 'export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.ustc.edu.cn/homebrew-core.git"' >> ~/.bash_profile

        # 对于 zsh 用户
        echo 'export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.ustc.edu.cn/homebrew-core.git"' >> ~/.zshrc

重置为官方地址：

::

    unset HOMEBREW_CORE_GIT_REMOTE
    git -C "$(brew --repo homebrew/core)" remote set-url origin https://github.com/Homebrew/homebrew-core

.. note::
    重置回默认远程后，用户应该删除 shell 的 profile 设置中的环境变量 ``HOMEBREW_CORE_GIT_REMOTE`` 以免运行 ``brew update`` 时远程再次被更换。

相关镜像
========
- :doc:`brew.git`
- :doc:`homebrew-bottles`
- :doc:`homebrew-cask.git`
- :doc:`homebrew-cask-versions.git`
- :doc:`linuxbrew-core.git`
- :doc:`linuxbrew-bottles`

相关链接
========

:官方主页: http://brew.sh/
:brew 文档: http://docs.brew.sh/
