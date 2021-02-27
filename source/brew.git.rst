===================
Homebrew 源使用帮助
===================

地址
====

https://mirrors.ustc.edu.cn/brew.git/

说明
====

Homebrew 源代码仓库

使用说明
========

替换 USTC 镜像：

::

    cd "$(brew --repo)"
    git remote set-url origin https://mirrors.ustc.edu.cn/brew.git

重置为官方地址：

::

    cd "$(brew --repo)"
    git remote set-url origin https://github.com/Homebrew/brew.git

.. note::
    初次安装 homebrew/linuxbrew 时，如果无法下载安装脚本，
    可以使用 `jsDelivr CDN <https://cdn.jsdelivr.net/gh/Homebrew/install@master/install.sh>`_ 
    下载 ``install.sh``，然后将脚本中的 ``HOMEBREW_BREW_GIT_REMOTE`` 
    变量对应的值修改为 ``https://mirrors.ustc.edu.cn/brew.git``。
    
    如有需要，脚本中的 ``HOMEBREW_CORE_GIT_REMOTE`` 变量可以修改为 :doc:`homebrew-core.git` 
    (macOS) 或 :doc:`linuxbrew-core.git` (Linux) 中对应的地址，以加快核心软件仓库索引下载的速度。

    由于 brew 安装脚本此前多次修改相关的变量名，也可以参考以下命令，将脚本中所有需要访问 GitHub 的 URL 替换为科大源:

    ::

        sed -e 's|https://github.com/Homebrew/homebrew-core|https://mirrors.ustc.edu.cn/homebrew-core.git|g' \
            -e 's|https://github.com/Homebrew/linuxbrew-core|https://mirrors.ustc.edu.cn/linuxbrew-core.git|g' \
            -e 's|https://github.com/Homebrew/brew|https://mirrors.ustc.edu.cn/brew.git|g' \
            -i.bak \
            install.sh

相关镜像
========
- :doc:`homebrew-bottles`
- :doc:`homebrew-core.git`
- :doc:`homebrew-cask.git`
- :doc:`homebrew-cask-versions.git`
- :doc:`linuxbrew-core.git`
- :doc:`linuxbrew-bottles`

相关链接
========

:官方主页: http://brew.sh/
:brew 文档: http://docs.brew.sh/
