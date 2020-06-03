
=====================
Nodesource 源使用帮助
=====================

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

将其中的 ``6.x`` 修改为自己所需的大版本号，如 8.x、10.x、12.x，将其中的stretch换为Debian相关版本对应的代号，其对应关系如下：

- Debian 8 / oldoldstable (Jessie)
- Debian 9 / oldstable (Stretch)
- Debian 10 / stable (Buster)
- Debian unstable (Sid)



Ubuntu 及衍生发行版使用说明
===========================

首先导入 GPG 密钥（若提示找不到 ``curl`` 命令，请先安装该包）

::

   curl -sSL https://deb.nodesource.com/gpgkey/nodesource.gpg.key | sudo apt-key add -

在 ``/etc/apt/sources.list`` 中添加

::

   deb https://mirrors.ustc.edu.cn/nodesource/deb/node_6.x xenial main
   deb-src https://mirrors.ustc.edu.cn/nodesource/deb/node_6.x xenial main

将其中的 ``6.x`` 修改为自己所需的大版本号，如 8.x、10.x、12.x，将其中的xenial换为Ubuntu对应的版本代号，Ubuntu版本号及其代号对应关系如下：

- Ubuntu 14.04 LTS (Trusty Tahr) - not available for Node.js 10 and later
- Ubuntu 16.04 LTS (Xenial Xerus)
- Ubuntu 18.04 LTS (Bionic Beaver)
- Ubuntu 18.10 (Cosmic Cuttlefish)
- Ubuntu 19.04 (Disco Dingo)
- Ubuntu 19.10 (Eoan Ermine)
- Ubuntu 20.04 LTS (Focal Fossa)

另外，考虑到Linux mint是基于Ubuntu相关版本衍生的，现将Linux mint与Ubuntu相关版本对应关系列出来，以方便使用Linux mint的用户使用。

- Linux Mint 17 "Qiana" (via Ubuntu 14.04 LTS) - not available for Node.js 10 and later
- Linux Mint 17.1 "Rebecca" (via Ubuntu 14.04 LTS) - not available for Node.js 10 and later
- Linux Mint 17.2 "Rafaela" (via Ubuntu 14.04 LTS) - not available for Node.js 10 and later
- Linux Mint 18 "Sarah" (via Ubuntu 16.04 LTS)
- Linux Mint 18.1 "Serena" (via Ubuntu 16.04 LTS)
- Linux Mint 18.2 "Sonya" (via Ubuntu 16.04 LTS)
- Linux Mint 18.3 "Sylvia" (via Ubuntu 16.04 LTS)
- Linux Mint Debian Edition (LMDE) 2 "Betsy" (via Debian 8)
- Linux Mint 19 "Tara" (via Ubuntu 18.04 LTS)
- Linux Mint 19.1 "Tessa" (via Ubuntu 18.04 LTS)
- Linux Mint 19.2 "Tina" (via Ubuntu 18.04 LTS)
- Linux Mint 19.3 "Tricia" (via Ubuntu 18.04 LTS)
- Linux Mint Debian Edition (LMDE) 3 "Cindy" (via Debian 9)
- Linux Mint Debian Edition (LMDE) 4 "Debbie" (via Debian 10)

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
