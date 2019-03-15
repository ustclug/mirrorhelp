=====================
Docker Hub 源使用帮助
=====================

地址
====

https://docker.mirrors.ustc.edu.cn/

说明
====

Docker Hub 镜像缓存

使用说明
========

Linux
-----

对于使用 upstart 的系统（Ubuntu 14.04、Debian 7 Wheezy），在配置文件 ``/etc/default/docker`` 中的 ``DOCKER_OPTS`` 中配置Hub地址：

::

    DOCKER_OPTS="--registry-mirror=https://docker.mirrors.ustc.edu.cn/"

重新启动服务:

::

    sudo service docker restart

对于使用 systemd 的系统（Ubuntu 16.04+、Debian 8+、CentOS 7）， 在配置文件 ``/etc/docker/daemon.json`` 中加入：

::

    {
      "registry-mirrors": ["https://docker.mirrors.ustc.edu.cn/"],
      "insecure-registries": []
    }

重新启动 dockerd：

::
  sudo systemctl daemon-reload
  sudo systemctl restart docker

macOS
-----

1. 打开 "Docker.app"
2. 进入偏好设置页面(快捷键 ``⌘,`` )
3. 打开 "Daemon" 选项卡
4. 在 "Registry mirrors" 中添加 ``https://docker.mirrors.ustc.edu.cn/``
5. 点击下方的 "Apply & Restart" 按钮

Windows
-------

在系统右下角托盘 Docker 图标内右键菜单选择 ``Settings`` ，打开配置窗口后左侧导航菜单选择 ``Daemon`` 。在 ``Registry mirrors`` 一栏中填写地址 ``https://docker.mirrors.ustc.edu.cn/`` ，之后点击 Apply 保存后 Docker 就会重启并应用配置的镜像地址了。

检查 Docker Hub 是否生效
------------------------

在命令行执行 ``docker info`` ，如果从结果中看到了如下内容，说明配置成功。

::

    Registry Mirrors:
        https://docker.mirrors.ustc.edu.cn/

相关链接
========

:Docker 主页: https://www.docker.com
:Docker Hub: https://hub.docker.com
