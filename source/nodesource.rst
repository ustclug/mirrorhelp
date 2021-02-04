=====================
Nodesource 源使用帮助
=====================

.. warning::
    由于上游原因，nodesource 仓库的同步无限期停止。我们建议选择使用 nvm 或 n 来管理系统中的 Node.js 环境。详见 :doc:`node`。

地址
====

https://mirrors.ustc.edu.cn/nodesource/

说明
====

Nodesource 仓库镜像

Debian 及衍生发行版使用说明
===========================

首先导入 GPG 密钥（若提示找不到 ``curl`` 命令，请先安装该包）

::

   curl -sSL https://deb.nodesource.com/gpgkey/nodesource.gpg.key | sudo apt-key add -

在 ``/etc/apt/sources.list`` 中添加

::

   deb https://mirrors.ustc.edu.cn/nodesource/deb/node_6.x stretch main
   deb-src https://mirrors.ustc.edu.cn/nodesource/deb/node_6.x stretch main

将其中的 ``6.x`` 修改为自己所需的大版本号即可，如 8.x、10.x。

RHEL 及衍生发行版使用说明
=========================

首先使用上游的配置脚本

::

   curl -sL https://rpm.nodesource.com/setup_6.x | bash -

此处需将 ``6.x`` 手动修改为所需大版本号。

修改 ``/etc/yum.repos.d/nodesource-*.repo`` 文件，将其中的所有
``rpm.nodesource.com`` 替换为 ``mirrors.ustc.edu.cn/nodesource/rpm``
即可。

相关链接
========

:官方说明: https://github.com/nodesource/distributions
