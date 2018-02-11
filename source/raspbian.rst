===================
Raspbian 源使用帮助
===================

地址
====

https://mirrors.nju.edu.cn/raspbian/

说明
====

Raspbian 安装镜像和软件源

系统架构
========

armhf

收录版本
========

* wheezy(oldoldstable)
* jessiels(oldstable)
* stretch(stable)
* buster(tesing)

使用说明
========

.. warning::
    操作前请做好相应备份

将 :file:`/etc/apt/sources.list` 文件中默认的源地址 ``http://mirrordirector.raspbian.org/`` 及 ``http://archive.raspbian.org/``
替换为 ``http://mirrors.nju.edu.cn/raspbian/`` 即可。

可以用以下命令替换：

::

  sudo sed -i 's|mirrordirector.raspbian.org|mirrors.nju.edu.cn/raspbian|g' /etc/apt/sources.list
  sudo sed -i 's|archive.raspbian.org|mirrors.nju.edu.cn/raspbian|g' /etc/apt/sources.list

当然也可以直接编辑 :file:`/etc/apt/sources.list` 文件（需要使用 sudo）。删除原文件所有内容，用以下内容取代（以 Stretch 示例）：

::

    deb http://mirrors.nju.edu.cn/raspbian/raspbian/ stretch main contrib non-free rpi
    #deb-src http://mirrors.nju.edu.cn/raspbian/raspbian/ stretch main contrib non-free rpi

编辑此文件后，请使用 ``sudo apt-get update`` 命令，更新软件索引。

同时也可能需要更改 archive.raspberrypi.org 源，请参考 :doc:`archive.raspberrypi.org` 。

相关链接
========

Raspbian 链接
  :Raspbian 主页: http://www.raspbian.org/
  :文档: http://www.raspbian.org/RaspbianDocumentation
  :Bug Tracker: http://www.raspbian.org/RaspbianBugs
  :镜像列表: http://www.raspbian.org/RaspbianMirrors

树莓派链接
  :树莓派基金会主页: https://www.raspberrypi.org/
  :树莓派基金会论坛 Raspbian 版块: https://www.raspberrypi.org/forums/viewforum.php?f=66
