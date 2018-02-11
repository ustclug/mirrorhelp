=========================
Debian-cdimage 源使用帮助
=========================

地址
====

https://mirrors.ustc.edu.cn/debian-cdimage/

说明
====

这是除了 ``debian-cd`` 之外 Debian 的另一部分补充用官方和准官方安装镜像的副本。
其内容来自 http://cdimage.debian.org/cdimage/ 但并未进行完整的同步，
保留了较实用的一部分内容。

该副本每周同步一次。

收录内容
========

站点暂时同步以下内容：

* 每周构建 testing 安装镜像 ``weekly-builds``
* 每周构建 testing LiveCD ``weekly-live-builds``
* 测试版 debian-installer 安装镜像与 LiveCD ``*_di_*``
* 含有非自由固件的准官方安装镜像 ``unofficial/non-free``
* 供 OpenStack 使用的 raw 镜像和 qcow2 镜像 ``openstack``
* 非正式发行架构（debian-ports）的安装镜像 ``ports``

.. tip::
    为节约服务器资源，我们不同步每日构建镜像。

使用说明
========

选择您需要的镜像文件下载使用即可。文件同目录下有文件散列值和数字签名文件，请进行校验以确保文件完整性。
