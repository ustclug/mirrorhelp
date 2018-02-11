===========================
Homebrew Bottles 源使用帮助
===========================

地址
====

https://mirrors.nju.edu.cn/homebrew-bottles/

说明
====

Homebrew 预编译二进制软件包

收录仓库
========

* homebrew/homebrew-core
* homebrew/homebrew-dupes
* homebrew/homebrew-php
* homebrew/homebrew-science
* homebrew/homebrew-nginx
* homebrew/homebrew-apache
* homebrew/homebrew-portable

使用说明
========

请在运行 brew 前设置环境变量 ``HOMEBREW_BOTTLE_DOMAIN`` ，值为 ``https://mirrors.nju.edu.cn/homebrew-bottles`` 。

对于 bash 用户：

::

    echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.nju.edu.cn/homebrew-bottles' >> ~/.bash_profile
    source ~/.bash_profile

对于 zsh 用户：

::

    echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.nju.edu.cn/homebrew-bottles' >> ~/.zshrc
    source ~/.zshrc

相关镜像
========
- :doc:`brew.git`
- :doc:`homebrew-core.git`

相关链接
========

:官方主页: http://brew.sh/
:Bottles 介绍: http://docs.brew.sh/Bottles.html
