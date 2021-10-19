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

    export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.ustc.edu.cn/linuxbrew-core.git"
    brew update

.. note::
    若用户设置了环境变量 ``HOMEBREW_CORE_GIT_REMOTE``，则每次运行 ``brew update`` 时将会自动设置远程。
    推荐用户将环境变量 ``HOMEBREW_CORE_GIT_REMOTE`` 加入 shell 的 profile 设置中。

    ::

        # 对于 bash 用户
        echo 'export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.ustc.edu.cn/linuxbrew-core.git"' >> ~/.bash_profile

        # 对于 zsh 用户
        echo 'export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.ustc.edu.cn/linuxbrew-core.git"' >> ~/.zshrc

重置为官方地址：

::

    unset HOMEBREW_CORE_GIT_REMOTE
    brew tap --custom-remote homebrew/core https://github.com/Homebrew/linuxbrew-core

.. note::
    若出现 ``Error: invalid option: --custom-remote`` 错误，请先运行 ``brew update`` 将 ``brew`` 更新至 3.2.17 或以上版本。
    重置回默认远程后，用户应该删除 shell 的 profile 设置中的环境变量 ``HOMEBREW_CORE_GIT_REMOTE`` 以免运行 ``brew update`` 时远程再次被更换。

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
