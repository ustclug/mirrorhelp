# ROS distributions

## 地址

<https://mirrors.ustc.edu.cn/rosdistro/>

## 说明

机器人操作系统（ROS）的依赖关系数据库，由 rosdep 使用。

## 使用说明

`rosdep` 默认的索引文件 `/etc/ros/rosdep/sources.list.d/20-default.list`
硬编码了 raw.githubusercontent.com 的地址，
因此需要手动修改该文件，参考步骤如下：

    # 使用以下步骤替代 rosdep init
    $ sudo mkdir -p /etc/ros/rosdep/sources.list.d/
    $ sudo curl -o /etc/ros/rosdep/sources.list.d/20-default.list https://mirrors.ustc.edu.cn/rosdistro/rosdep/sources.list.d/20-default.list
    $ sed -i 's#raw.githubusercontent.com/ros/rosdistro/master#mirrors.ustc.edu.cn/rosdistro#g' /etc/ros/rosdep/sources.list.d/20-default.list

    # 更换源
    $ export ROSDISTRO_INDEX_URL=https://mirrors.ustc.edu.cn/rosdistro/index-v4.yaml
    $ rosdep update

    # 可以考虑持久化以上环境变量：
    $ echo 'export ROSDISTRO_INDEX_URL=https://mirrors.ustc.edu.cn/rosdistro/index-v4.yaml' >> ~/.bashrc

本帮助参考了 [TUNA 的 rosdistro
帮助](https://mirrors.tuna.tsinghua.edu.cn/help/rosdistro/) 编写。

## 相关镜像

-   `ros`{.interpreted-text role="doc"}

## 相关链接

仓库链接

:   <https://github.com/ros/rosdistro>
