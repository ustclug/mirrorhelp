========================
ROS 源使用帮助
========================

地址
====

https://mirrors.ustc.edu.cn/ros/

说明
====

机器人操作系统（ROS）的软件源镜像。

使用说明
========

Ubuntu, Debian
------------------------------

1. 将软件源添加至系统::

    sudo sh -c 'echo "deb https://mirrors.ustc.edu.cn/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

如果 IPv6 地址无效导致无法刷新软件源信息，将 ``mirrors.ustc.edu.cn`` 改成 ``ipv4.mirrors.ustc.edu.cn`` 以强制使用 IPv4。

2. 导入key::

    sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116

如果此服务器不可用，可以尝试换用 ``hkp://pgp.mit.edu:80`` 或 ``hkp://keyserver.ubuntu.com:80``。

3. 刷新软件源缓存 ``sudo apt update``。

相关链接
========

:项目主页: http://www.ros.org/
