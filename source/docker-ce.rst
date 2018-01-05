====================
Docker CE 源使用帮助
====================

地址
====

https://mirrors.ustc.edu.cn/docker-ce/

说明
====

Docker CE 仓库镜像

收录架构
========

所有 Docker CE 官方支持的架构

收录版本
========

所有 Docker CE 官方支持的版本

收录平台
========

所有 Docker CE 官方支持的平台（包括 Linux、Windows、macOS），
具体请查看 `官方说明 <https://docs.docker.com/engine/installation/#supported-platforms>`_ 。

使用说明
========

安装 Docker CE，请按照 `官方安装文档 <https://docs.docker.com/engine/installation/>`_ ，选择你对应的系统。
以 Ubuntu 为例，参考 `官方 Ubuntu 安装 Docker CE 手册 <https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/>`_ 进行安装。
在阅读官方安装手册时，只要把 ``download.docker.com`` 地址换成 ``mirrors.ustc.edu.cn/docker-ce`` 即可。

.. tip::
    以上 Docker CE 的官方文档有中文版，但更新可能不如英文版及时，请移步 https://docs.docker-cn.com/engine/installation/ 。

.. tip::
    安装完 Docker CE 之后，替换掉官方的 Docker Registry 服务，可加快拉取 Docker 镜像的速度，请参考 :doc:`dockerhub` 。

相关链接
========

:Docker 官网: https://www.docker.com/
:Docker Store: https://store.docker.com/
:Docker Hub: https://hub.docker.com/
