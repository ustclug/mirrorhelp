=================
Fedora 源使用帮助
=================

地址
====

https://mirrors.ustc.edu.cn/fedora/

说明
====

Fedora 软件源

收录架构
========

x86_64

收录版本
========

所有仍在支持的版本和最新测试版本

使用说明
========


以root运行以下脚本或者手动操作

.. literalinclude:: includes/fedora.ustcfy.sh

.. warning::
    操作前请做好相应备份。

将以下内容保存到 :file:`/etc/yum.repos.d/fedora.repo` 文件：

.. literalinclude:: includes/fedora.repo

将以下内容保存到 :file:`/etc/yum.repos.d/fedora-updates.repo` 文件：

.. literalinclude:: includes/fedora-updates.repo

将以下内容保存到 :file:`/etc/yum.repos.d/fedora-modular.repo` 文件：

.. literalinclude:: includes/fedora-modular.repo

将以下内容保存到 :file:`/etc/yum.repos.d/fedora-updates-modular.repo` 文件：

.. literalinclude:: includes/fedora-updates-modular.repo

最后运行 ``sudo dnf makecache`` 生成缓存。

相关链接
========

:官方主页: https://getfedora.org/
:邮件列表: https://fedoraproject.org/wiki/Communicating_and_getting_help
:论坛: https://forums.fedoraforum.org/
:文档: https://docs.fedoraproject.org/
:Wiki: https://fedoraproject.org/wiki/
:镜像列表: https://admin.fedoraproject.org/mirrormanager
