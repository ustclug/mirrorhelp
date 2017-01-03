===================
Ubuntu 镜像使用帮助
===================

镜像地址
========

https://mirrors.ustc.edu.cn/ubuntu/

收录架构
========

AMD64 (x86_64), Intel x86

收录版本
========

所有 Ubuntu 当前支持的版本，包括开发版，具体版本见 https://wiki.ubuntu.com/Releases

对于 Ubuntu 不再支持的版本，请参考 :doc:`ubuntu-old-release`

使用说明
========

软件包管理中心（推荐）
----------------------

在软件包管理中心“软件源”中选择“中国的服务器”下 mirrors.ustc.edu.cn 即可自动使用。

手动更改配置文件
----------------

.. warning::
    操作前请做好相应备份

一般情况下，更改 ``/etc/apt/sources.list`` 文件中 Ubuntu 默认的源地址 ``http://archive.ubuntu.com/``
为 ``http://mirrors.ustc.edu.cn`` 即可。

可以使用如下命令：

::

  sudo sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list

当然直接编辑 /etc/apt/sources.list 文件（需要使用 sudo）也可以，以 Ubuntu 16.04 为例，在文件最前面添加以下条目：

::

    deb http://mirrors.ustc.edu.cn/ubuntu/ xenial main restricted universe multiverse
    deb http://mirrors.ustc.edu.cn/ubuntu/ xenial-security main restricted universe multiverse
    deb http://mirrors.ustc.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse
    deb http://mirrors.ustc.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
    deb-src http://mirrors.ustc.edu.cn/ubuntu/ xenial main restricted universe multiverse
    deb-src http://mirrors.ustc.edu.cn/ubuntu/ xenial-security main restricted universe multiverse
    deb-src http://mirrors.ustc.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse
    deb-src http://mirrors.ustc.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse

另外，也可以 snullp 大叔开发的 `配置生成器 <https://mirrors.ustc.edu.cn/repogen>`_ 。

相关链接
========

:官方主页: http://www.ubuntu.com/
:邮件列表: http://www.ubuntu.com/support/community/mailinglists
:论坛: http://ubuntuforums.org/
:中文论坛: http://forum.ubuntu.org.cn/
:Wiki: https://wiki.ubuntu.com/
:文档: https://help.ubuntu.com/
