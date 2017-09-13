========================
RPM Fusion 源使用帮助
========================

地址
====

https://mirrors.ustc.edu.cn/rpmfusion/

说明
====

RPM Fusion 是为 Fedora/RHEL 提供额外 rpm 软件包的第三方软件源。

使用说明
========

使用下列命令，可以同时启用其 ``free`` 和 ``nonfree`` 软件源：

Fedora 22+
-----------

::

    su -c 'dnf install http://mirrors.ustc.edu.cn/rpmfusion/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm http://mirrors.ustc.edu.cn/rpmfusion/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm'

Fedora 14 至 Fedora 21
----------------------

::

    su -c 'yum install --nogpgcheck http://mirrors.ustc.edu.cn/rpmfusion/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm http://mirrors.ustc.edu.cn/rpmfusion/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm'

RHEL 5 或兼容系统
-----------------

::

    su -c 'rpm -Uvh http://mirrors.ustc.edu.cn/rpmfusion/free/el/updates/5/i386/rpmfusion-free-release-5-1.noarch.rpm http://mirrors.ustc.edu.cn/rpmfusion/nonfree/el/updates/5/i386/rpmfusion-nonfree-release-5-1.noarch.rpm'

RHEL 6 或兼容系统
-----------------

::

    su -c 'yum localinstall --nogpgcheck http://mirrors.ustc.edu.cn/rpmfusion/free/el/updates/6/i386/rpmfusion-free-release-6-1.noarch.rpm http://mirrors.ustc.edu.cn/rpmfusion/nonfree/el/updates/6/i386/rpmfusion-nonfree-release-6-1.noarch.rpm'

备注
====

安装好以上 rpm （主要包括 rpmfusion 相应的 repo 文件）后，您可能需要再运行：

::

    sudo yum makecache

以更新缓存。根据版本不同，可能需要将 ``yum`` 替换为 ``dnf`` 。

在 RHEL 或兼容发行版上，您可能需要预先启用 EPEL 源，请参考 :doc:`epel`。

未尽内容，请参阅官方配置指南（链接附后）。

相关链接
========

:项目主页: http://rpmfusion.org
:邮件列表: http://lists.rpmfusion.org
:用户配置指南（英文）: http://rpmfusion.org/Configuration
