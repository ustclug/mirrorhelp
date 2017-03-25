=====================
Docker CE 源使用帮助
=====================

地址
====

https://mirrors.ustc.edu.cn/docke-ce/

说明
====

Docker CE 仓库镜像

使用说明
========

Ubuntu
-----

添加镜像仓库

:: 
    sudo apt-get -y install \
    apt-transport-https \
    ca-certificates \
    curl

    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

    sudo add-apt-repository \
       "deb [arch=amd64] http://mirrors.ustc.edu.cn/docker-ce/linux/ubuntu \
       $(lsb_release -cs) \
       stable"
      
安装Docker-CE

::
    sudo apt-get -y install docker-ce

macOS
-----

.. todo: macOS平台的使用方法

Windows
-------

.. todo:: windows平台的使用方法

相关链接
========

:Docker 主页: https://www.docker.com
:Docker Hub: https://hub.docker.com
