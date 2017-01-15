========================
Gentoo-Portage 源使用帮助
========================

地址
====

https://mirrors.ustc.edu.cn/gentoo-portage/

说明
====

Gentoo-Portage 软件源

收录架构
====

ALL

使用说明
========

新建或修改 :file:`/etc/portage/repos.conf` ： 

::

  [DEFAULT]
  main-repo = gentoo

  [gentoo]
  location = /usr/portage
  sync-type = rsync
  sync-uri = rsync://rsync.mirrors.ustc.edu.cn/gentoo-portage/
  auto-sync = yes

相关链接
========

:官方主页: https://www.gentoo.org/
:邮件列表: https://www.gentoo.org/main/en/lists.xml
:论坛: https://forums.gentoo.org/
:文档: https://www.gentoo.org/doc/en/
:Wiki: https://wiki.gentoo.org/
:镜像列表: https://www.gentoo.org/main/en/mirrors-rsync.xml
