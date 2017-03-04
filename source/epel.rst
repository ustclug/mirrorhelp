========================================
EPEL 源使用帮助
========================================

地址
==============================

https://mirrors.ustc.edu.cn/epel/

说明
==============================

EPEL (Extra Packages for Enterprise Linux) 是由 Fedora Special Interest Group 为企业 Linux 创建、维护和管理的一个高质量附加包集合，适用于但不仅限于 Red Hat Enterprise Linux (RHEL), CentOS, Scientific Linux (SL), Oracle Linux (OL)

收录架构
==============================

官方支持的所有架构

收录版本
==============================

官方支持的所有版本

使用说明
==============================

执行以下命令：

::

  sudo yum install -y epel-release
  sudo sed -e 's!^mirrorlist=!#mirrorlist=!g' \
           -e 's!^#baseurl=!baseurl=!g' \
           -e 's!//download\.fedoraproject\.org/pub!//mirrors.ustc.edu.cn!g' \
           -e 's!http://mirrors\.ustc!https://mirrors.ustc!g' \
           -i /etc/yum.repos.d/epel.repo /etc/yum.repos.d/epel-testing.repo

相关链接
==============================

:WIKI: http://fedoraproject.org/wiki/EPEL
:FAQ: http://fedoraproject.org/wiki/EPEL/faq
