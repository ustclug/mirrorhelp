=================
CentOS 源使用帮助
=================

地址
====

https://mirrors.ustc.edu.cn/centos/

说明
====

CentOS 软件源

收录架构
========

x86_64, i386

收录版本
========

6, 7, 8

使用说明
========

.. warning::
    操作前请做好相应备份。

对于 CentOS 8，使用以下命令替换默认的配置

::

  sudo sed -e 's|^mirrorlist=|#mirrorlist=|g' \
           -e 's|^#baseurl=http://mirror.centos.org/$contentdir|baseurl=https://mirrors.ustc.edu.cn/centos|g' \
           -i.bak \
           /etc/yum.repos.d/CentOS-Base.repo \
           /etc/yum.repos.d/CentOS-Extras.repo \
           /etc/yum.repos.d/CentOS-AppStream.repo

对于 CentOS 6、7，使用以下命令替换默认配置

::

  sudo sed -e 's|^mirrorlist=|#mirrorlist=|g' \
           -e 's|^#baseurl=http://mirror.centos.org/centos|baseurl=https://mirrors.ustc.edu.cn/centos|g' \
           -i.bak \
           /etc/yum.repos.d/CentOS-Base.repo

以上命令只替换了默认启用的仓库。替换之后请运行 ``yum makecache`` 更新缓存。

以下是替换之后的文件：

* CentOS 8：

  :file:`/etc/yum.repos.d/CentOS-Base.repo` 文件：

  .. literalinclude:: includes/centos8/CentOS-Base.repo

  :file:`/etc/yum.repos.d/CentOS-Extras.repo` 文件：

  .. literalinclude:: includes/centos8/CentOS-Extras.repo

  :file:`/etc/yum.repos.d/CentOS-AppStream.repo` 文件：

  .. literalinclude:: includes/centos8/CentOS-AppStream.repo

* CentOS 7：

  :file:`/etc/yum.repos.d/CentOS-Base.repo` 文件：

  .. literalinclude:: includes/centos7/CentOS-Base.repo

* CentOS 6：

  :file:`/etc/yum.repos.d/CentOS-Base.repo` 文件：

  .. literalinclude:: includes/centos6/CentOS-Base.repo

相关链接
========

:官方主页: https://www.centos.org/
:邮件列表: https://www.centos.org/modules/tinycontent/index.php?id=16
:论坛: https://www.centos.org/modules/newbb/
:文档: https://www.centos.org/docs/
:Wiki: https://wiki.centos.org/
:镜像列表: https://www.centos.org/modules/tinycontent/index.php?id=32
