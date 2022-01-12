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

1. 导入软件源的 GPG key::

    sudo sh -c 'echo "deb https://mirrors.ustc.edu.cn/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
    
    sudo apt update && sudo apt install curl gnupg2 lsb-release
    sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg

2. 添加软件源::

    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(source /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

3. 刷新软件源缓存 ``sudo apt update``，安装所需的 ROS 发行版。

相关链接
========

:项目主页: http://www.ros.org/
