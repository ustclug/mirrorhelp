===========================
Homebrew Bottles 源使用帮助
===========================

地址
====

https://mirrors.ustc.edu.cn/homebrew-bottles/

说明
====

Homebrew 预编译二进制软件包与软件包元数据文件

收录仓库
========

* homebrew/homebrew-core
* brew formula 与 cask 的 JSON 元数据文件

使用说明
========

请在运行 ``brew`` 前设置环境变量 ``HOMEBREW_BOTTLE_DOMAIN``，值为 ``https://mirrors.ustc.edu.cn/homebrew-bottles``。

此外，brew 4.0 及之后的版本使用新的元数据 JSON API 接口，因此还需要设置环境变量 ``HOMEBREW_API_DOMAIN``，值为 ``https://mirrors.ustc.edu.cn/homebrew-bottles/api``。

临时替换：

::

    export HOMEBREW_BOTTLE_DOMAIN="https://mirrors.ustc.edu.cn/homebrew-bottles"
    export HOMEBREW_API_DOMAIN="https://mirrors.ustc.edu.cn/homebrew-bottles/api"

永久替换：

::

    # 对于 bash 用户
    echo 'export HOMEBREW_BOTTLE_DOMAIN="https://mirrors.ustc.edu.cn/homebrew-bottles"' >> ~/.bash_profile
    echo 'export HOMEBREW_API_DOMAIN="https://mirrors.ustc.edu.cn/homebrew-bottles/api"' >> ~/.bash_profile

    # 对于 zsh 用户
    echo 'export HOMEBREW_BOTTLE_DOMAIN="https://mirrors.ustc.edu.cn/homebrew-bottles"' >> ~/.zshrc
    echo 'export HOMEBREW_API_DOMAIN="https://mirrors.ustc.edu.cn/homebrew-bottles/api"' >> ~/.zshrc

.. note::
    Linuxbrew 核心仓库（``linuxbrew-core``）自 2021 年 10 月 25 日（``brew`` 版本 3.3.0 起）被弃用，Linuxbrew 用户应迁移至 ``homebrew-core``。
    Linuxbrew 用户请依本镜像说明重新设置镜像。

相关镜像
========
- :doc:`brew.git`
- :doc:`homebrew-core.git`
- :doc:`homebrew-cask.git`
- :doc:`homebrew-cask-versions.git`

相关链接
========

:官方主页: http://brew.sh/
:Bottles 介绍: http://docs.brew.sh/Bottles.html
