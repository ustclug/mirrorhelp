# ROS2

## 地址

<https://mirrors.ustc.edu.cn/ros/>

## 说明

机器人操作系统（ROS）2 的软件源镜像。

## 使用说明

### Ubuntu, Debian

1. 导入 key:

    ```shell
    sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
    ```

2. 将软件源添加至系统：

    ```shell
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://mirrors.ustc.edu.cn/ros2/ubuntu $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
    ```

3. 刷新软件源缓存 `sudo apt update`，安装所需的 ROS2 发行版。

## 相关镜像

- [rosdistro](rosdistro.md)

## 相关链接

项目主页

:   <http://www.ros.org/>
