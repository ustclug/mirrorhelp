============================
Linuxbrew Bottles 源使用帮助
============================

地址
====

https://mirrors.ustc.edu.cn/linuxbrew-bottles/

说明
====

Linuxbrew 预编译二进制软件包

收录仓库
========

* homebrew/linuxbrew-core

使用说明
========

请在运行 brew 前设置环境变量 ``HOMEBREW_BOTTLE_DOMAIN`` ，值为 ``https://mirrors.ustc.edu.cn/linuxbrew-bottles`` 。

对于 bash 用户：

::

    echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/linuxbrew-bottles' >> ~/.bash_profile
    source ~/.bash_profile

对于 zsh 用户：

::

    echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/linuxbrew-bottles' >> ~/.zshrc
    source ~/.zshrc

相关镜像
========
- :doc:`brew.git`
- :doc:`linuxbrew-core.git`

相关链接
========

:官方主页: https://brew.sh/
:Bottles 介绍: https://docs.brew.sh/Bottles.html
