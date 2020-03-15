=================
CentOS 源使用帮助
=================

地址
====

https://mirrors.ustc.edu.cn/centos/

说明
====

CentOS 软件源.

收录架构
========

x86_64, i386

收录版本
========

5, 6, 7, 8

使用说明
========

首先备份 :file:`CentOS-Base.repo` 

::

  mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
  
对于 CentOS 8 需要删除重复的 :file:`repo`

::

  rm -f /etc/yum.repos.d/CentOS-AppStream.repo /etc/yum.repos.d/CentOS-PowerTools.repo /etc/yum.repos.d/CentOS-centosplus.repo /etc/yum.repos.d/CentOS-Extras.repo
  
接着复制对应版本的 :file:`CentOS-Base.repo` , 放入 :file:`/etc/yum.repos.d/CentOS-Base.repo`

这是 CentOS 5 的： 

::

  # CentOS-Base.repo
  #
  # The mirror system uses the connecting IP address of the client and the
  # update status of each mirror to pick mirrors that are updated to and
  # geographically close to the client.  You should use this for CentOS updates
  # unless you are manually picking other mirrors.
  #
  # If the mirrorlist= does not work for you, as a fall back you can try the 
  # remarked out baseurl= line instead.
  #
  #

  [base]
  name=CentOS-$releasever - Base - mirrors.ustc.edu.cn
  baseurl=https://mirrors.ustc.edu.cn/centos/$releasever/os/$basearch/
  #mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=os
  gpgcheck=1
  gpgkey=https://mirrors.ustc.edu.cn/centos/RPM-GPG-KEY-CentOS-5

  #released updates 
  [updates]
  name=CentOS-$releasever - Updates - mirrors.ustc.edu.cn
  baseurl=https://mirrors.ustc.edu.cn/centos/$releasever/updates/$basearch/
  #mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=updates
  gpgcheck=
  gpgkey=https://mirrors.ustc.edu.cn/centos/RPM-GPG-KEY-CentOS-5

  #additional packages that may be useful
  [extras]
  name=CentOS-$releasever - Extras - mirrors.ustc.edu.cn
  baseurl=https://mirrors.ustc.edu.cn/centos/$releasever/extras/$basearch/
  #mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=extras
  gpgcheck=1
  gpgkey=https://mirrors.ustc.edu.cn/centos/RPM-GPG-KEY-CentOS-5

  #packages used/produced in the build but not released
  [addons]
  name=CentOS-$releasever - Addons - mirrors.ustc.edu.cn
  baseurl=https://mirrors.ustc.edu.cn/centos/$releasever/addons/$basearch/
  #mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=addons
  gpgcheck=1
  gpgkey=https://mirror.centos.org/centos/RPM-GPG-KEY-CentOS-5

  #additional packages that extend functionality of existing packages
  [centosplus]
  name=CentOS-$releasever - Plus - mirrors.ustc.edu.cn
  baseurl=https://mirrors.ustc.edu.cn/centos/$releasever/centosplus/$basearch/
  #mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=centosplus
  gpgcheck=1
  enabled=0
  gpgkey=https://mirrors.ustc.edu.cn/centos/RPM-GPG-KEY-CentOS-5

  #contrib - packages by Centos Users
  [contrib]
  name=CentOS-$releasever - Contrib - mirrors.ustc.edu.cn
  baseurl=https://mirrors.ustc.edu.cn/centos/$releasever/contrib/$basearch/
  #mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=contrib
  gpgcheck=1
  enabled=0
  gpgkey=https://mirrors.ustc.edu.cn/centos/RPM-GPG-KEY-CentOS-5

这是 CentOS 6 的： 

::

  # CentOS-Base.repo
  #
  # The mirror system uses the connecting IP address of the client and the
  # update status of each mirror to pick mirrors that are updated to and
  # geographically close to the client.  You should use this for CentOS updates
  # unless you are manually picking other mirrors.
  #
  # If the mirrorlist= does not work for you, as a fall back you can try the 
  # remarked out baseurl= line instead.
  #
  #

  [base]
  name=CentOS-$releasever - Base - mirrors.ustc.edu.cn
  baseurl=https://mirrors.ustc.edu.cn/centos/$releasever/os/$basearch/
  #mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=os
  gpgcheck=1
  gpgkey=https://mirrors.ustc.edu.cn/centos/RPM-GPG-KEY-CentOS-6

  #released updates 
  [updates]
  name=CentOS-$releasever - Updates - mirrors.ustc.edu.cn
  baseurl=https://mirrors.ustc.edu.cn/centos/$releasever/updates/$basearch/
  #mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=updates
  gpgcheck=1
  gpgkey=https://mirrors.ustc.edu.cn/centos/RPM-GPG-KEY-CentOS-6

  #additional packages that may be useful
  [extras]
  name=CentOS-$releasever - Extras - mirrors.ustc.edu.cn
  baseurl=https://mirrors.ustc.edu.cn/centos/$releasever/extras/$basearch/
  #mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=extras
  gpgcheck=1
  gpgkey=https://mirrors.ustc.edu.cn/centos/RPM-GPG-KEY-CentOS-6

  #additional packages that extend functionality of existing packages
  [centosplus]
  name=CentOS-$releasever - Plus - mirrors.ustc.edu.cn
  baseurl=https://mirrors.ustc.edu.cn/centos/$releasever/centosplus/$basearch/
  #mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=centosplus
  gpgcheck=1
  enabled=0
  gpgkey=https://mirrors.ustc.edu.cn/centos/RPM-GPG-KEY-CentOS-6

  #contrib - packages by Centos Users
  [contrib]
  name=CentOS-$releasever - Contrib - mirrors.ustc.edu.cn
  baseurl=https://mirrors.ustc.edu.cn/centos/$releasever/contrib/$basearch/
  #mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=contrib
  gpgcheck=1
  enabled=0
  gpgkey=https://mirrors.ustc.edu.cn/centos/RPM-GPG-KEY-CentOS-6
  
这是 CentOS 7 的： 

::

  # CentOS-Base.repo
  #
  # The mirror system uses the connecting IP address of the client and the
  # update status of each mirror to pick mirrors that are updated to and
  # geographically close to the client.  You should use this for CentOS updates
  # unless you are manually picking other mirrors.
  #
  # If the mirrorlist= does not work for you, as a fall back you can try the
  # remarked out baseurl= line instead.
  #
  #

  [base]
  name=CentOS-$releasever - Base
  #mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=os
  baseurl=https://mirrors.ustc.edu.cn/centos/$releasever/os/$basearch/
  gpgcheck=1
  gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

  #released updates
  [updates]
  name=CentOS-$releasever - Updates
  # mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=updates
  baseurl=https://mirrors.ustc.edu.cn/centos/$releasever/updates/$basearch/
  gpgcheck=1
  gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

  #additional packages that may be useful
  [extras]
  name=CentOS-$releasever - Extras
  # mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=extras
  baseurl=https://mirrors.ustc.edu.cn/centos/$releasever/extras/$basearch/
  gpgcheck=1
  gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

  #additional packages that extend functionality of existing packages
  [centosplus]
  name=CentOS-$releasever - Plus
  # mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=centosplus
  baseurl=https://mirrors.ustc.edu.cn/centos/$releasever/centosplus/$basearch/
  gpgcheck=1
  enabled=0
  gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
  
这是 CentOS 8 的： 
::

  # CentOS-Base.repo
  #
  # The mirror system uses the connecting IP address of the client and the
  # update status of each mirror to pick mirrors that are updated to and
  # geographically close to the client.  You should use this for CentOS updates
  # unless you are manually picking other mirrors.
  #
  # If the mirrorlist= does not work for you, as a fall back you can try the
  # remarked out baseurl= line instead.
  #
  #

  [BaseOS]
  name=CentOS-$releasever - Base
  #mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=BaseOS&infra=$infra
  baseurl=https://mirrors.ustc.edu.cn/centos/$releasever/BaseOS/$basearch/os/
  gpgcheck=1
  enabled=1
  gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial
  
  #additional packages that may be useful
  [Extras]
  name=CentOS-$releasever - Extras
  #mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=extras&infra=$infra
  baseurl=https://mirrors.ustc.edu.cn/centos/$releasever/extras/$basearch/os/
  gpgcheck=1
  enabled=1
  gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial

  #additional packages that extend functionality of existing packages
  [centosplus]
  name=CentOS-$releasever - Plus
  #mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=centosplus&infra=$infra
  baseurl=https://mirrors.ustc.edu.cn/centos/$releasever/centosplus/$basearch/os/
  gpgcheck=1
  enabled=0
  gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial

  [AppStream]
  name=CentOS-$releasever - AppStream
  #mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=AppStream&infra=$infra
  baseurl=https://mirrors.ustc.edu.cn/centos/$releasever/AppStream/$basearch/os/
  gpgcheck=1
  enabled=1
  gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial

  [PowerTools]
  name=CentOS-$releasever - PowerTools
  #mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=PowerTools&infra=$infra
  baseurl=https://mirrors.ustc.edu.cn/centos/$releasever/PowerTools/$basearch/os/
  gpgcheck=1
  enabled=0
  gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial

最后运行 ``sudo yum makecache`` 生成缓存。

相关链接
========

:官方主页: https://www.centos.org/
:邮件列表: https://www.centos.org/modules/tinycontent/index.php?id=16
:论坛: https://www.centos.org/modules/newbb/
:文档: https://www.centos.org/docs/
:Wiki: https://wiki.centos.org/
:镜像列表: https://www.centos.org/modules/tinycontent/index.php?id=32
