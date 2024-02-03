===================
MySQL 源使用帮助
===================

地址
====

https://mirrors.ustc.edu.cn/mysql-repo/

说明
====

MySQL 软件仓库镜像

收录版本
========

目前仍被支持的 Linux 发行版的 MySQL APT/YUM 软件包（不含调试符号）。

文件目录结构与上游保持一致。

使用说明
========

Debian/Ubuntu 用户参考以下帮助文档配置：https://dev.mysql.com/doc/mysql-apt-repo-quick-guide/en/\ 。

RHEL/Fedora 用户参考以下帮助文档配置：https://dev.mysql.com/doc/mysql-yum-repo-quick-guide/en/\ 。

在安装配置软件源的 deb 或 rpm 包后，将 ``/etc/apt/sources.list.d/mysql.list``
或 ``/etc/yum.repos.d/mysql-community.repo`` 中的 ``repo.mysql.com``
替换为 ``mirrors.ustc.edu.cn/mysql-repo`` 即可。

相关链接
========

:上游仓库: https://repo.mysql.com/
