=================================
Homebrew Services 源使用帮助
=================================

地址
====

https://mirrors.ustc.edu.cn/homebrew-services.git/

说明
====

与 ``brew services`` 有关的文件，用于在 macOS (``launchctl``) 与 Linux (``systemctl``) 上管理 brew 安装的服务。

使用说明
========

使用 USTC 镜像安装，或将已安装的仓库远程替换为 USTC 镜像：

::

    brew tap --custom-remote --force-auto-update homebrew/services https://mirrors.ustc.edu.cn/homebrew-services.git

.. note::
    若出现 ``Error: invalid option: --custom-remote`` 错误，请先运行 ``brew update`` 将 ``brew`` 更新至 3.2.17 或以上版本。

重置为官方地址：

::

    brew tap --custom-remote --force-auto-update homebrew/services https://github.com/Homebrew/homebrew-services


相关镜像
========
- :doc:`brew.git`
- :doc:`homebrew-bottles`
- :doc:`homebrew-core.git`
- :doc:`homebrew-cask.git`
- :doc:`homebrew-cask-versions.git`

相关链接
========

:官方主页: https://github.com/Homebrew/homebrew-services
:Homebrew: https://brew.sh/
