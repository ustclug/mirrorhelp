=========================
Gentoo Portage 源使用帮助
=========================

地址
====

https://mirrors.ustc.edu.cn/gentoo.git

说明
====

Gentoo Portage Ebuild 源 (Git同步)

收录架构
========

ALL

使用说明
========

请确保系统中已安装 ``dev-vcs/git``

修改 :file:`/etc/portage/repos.conf/gentoo.conf`中的：

``sync-type`` 为 ``git``

``sync-uri`` 为 ``https://mirrors.ustc.edu.cn/gentoo.git``

以下是修改后的

::

  [DEFAULT]
  main-repo = gentoo

  [gentoo]
  location = /var/db/repos/gentoo
  sync-type = git
  sync-uri = https://mirrors.ustc.edu.cn/gentoo.git
  auto-sync = yes
  sync-rsync-verify-jobs = 1
  sync-rsync-verify-metamanifest = yes
  sync-rsync-verify-max-age = 24
  sync-openpgp-key-path = /usr/share/openpgp-keys/gentoo-release.asc
  sync-openpgp-keyserver = hkps://keys.gentoo.org
  sync-openpgp-key-refresh-retry-count = 40
  sync-openpgp-key-refresh-retry-overall-timeout = 1200
  sync-openpgp-key-refresh-retry-delay-exp-base = 2
  sync-openpgp-key-refresh-retry-delay-max = 60
  sync-openpgp-key-refresh-retry-delay-mult = 4
  sync-webrsync-verify-signature = yes

然后：

* 删除本地main tree: ``rm -rf /var/db/repos/gentoo/``

* 重新同步(使用git): ``emerge --sync``

.. note::
    需要 ``root`` 用户或者 ``sudo`` 才能完成上述操作

相关链接
========

:官方主页: https://www.gentoo.org/
:邮件列表: https://www.gentoo.org/main/en/lists.xml
:论坛: https://forums.gentoo.org/
:文档: https://www.gentoo.org/doc/en/
:Wiki: https://wiki.gentoo.org/
:镜像列表: https://www.gentoo.org/main/en/mirrors-rsync.xml
