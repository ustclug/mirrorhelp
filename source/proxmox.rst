======================
Proxmox 源使用帮助
======================

地址
====

https://mirrors.ustc.edu.cn/proxmox/

说明
====

Proxmox 软件源

收录架构
========

所有 Proxmox 官方支持的架构


收录版本
========

所有 Proxmox 官方支持的版本


使用说明
========


.. warning::
    操作前请做好相应备份

Debian，Proxmox
------------------------------

一般情况下，需要同时修改基础系统（Debian）的源文件 :file:`/etc/apt/sources.list` 和Proxmox的源文件。

修改基础系统（Debian）的源文件，可以使用如下命令：

::

  sed -i 's|^deb http://ftp.debian.org|deb https://mirrors.ustc.edu.cn|g' /etc/apt/sources.list
  sed -i 's|^deb http://security.debian.org|deb https://mirrors.ustc.edu.cn/debian-security|g' /etc/apt/sources.list

修改Proxmox的源文件，可以使用如下命令：

::

  CODENAME=`cat /etc/os-release |grep CODENAME |cut -f 2 -d "="`
  echo "deb https://mirrors.ustc.edu.cn/proxmox/debian/pve $CODENAME pve-no-subscription" > /etc/apt/sources.list.d/pve-no-subscription.list


更改完 :file:`sources.list` 文件后请运行 ``apt update`` 更新索引以生效。


CT Templates
------------------------------

另外，如果你需要使用Proxmox网页端下载CT Templates，可以替换CT Templates的源为``http://mirrors.ustc.edu.cn``。

具体方法：将 :file:`/usr/share/perl5/PVE/APLInfo.pm` 文件中默认的源地址 ``http://download.proxmox.com``
替换为 ``https://mirrors.ustc.edu.cn/proxmox`` 即可。

可以使用如下命令：

::

  cp /usr/share/perl5/PVE/APLInfo.pm /usr/share/perl5/PVE/APLInfo.pm_back
  sed -i 's|http://download.proxmox.com|https://mirrors.ustc.edu.cn/proxmox|g' /usr/share/perl5/PVE/APLInfo.pm 

针对file:`/usr/share/perl5/PVE/APLInfo.pm` 文件的修改，重启后生效。

