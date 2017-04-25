=====================
Docker Hub 源使用帮助
=====================

地址
====

http://docker.mirrors.ustc.edu.cn/

说明
====

Docker Hub 镜像缓存

使用说明
========

Linux
-----

在配置文件 ``/etc/docker/daemon.json`` 中加入：

::

    {
      "registry-mirrors": ["http://docker.mirrors.ustc.edu.cn/"]
    }

重新启动dockerd：

::

  sudo service docker restart

macOS
-----

1. 打开 "Docker.app"
2. 进入偏好设置页面(快捷键 ``⌘,`` )
3. 打开 "Advanced" 选项卡
4. 在 "Registry mirrors" 中添加 ``http://docker.mirrors.ustc.edu.cn/``
5. 点击下方的 "Restart" 按钮

Windows
-------

.. todo:: windows平台的使用方法

相关链接
========

:Docker 主页: https://www.docker.com
:Docker Hub: https://hub.docker.com
