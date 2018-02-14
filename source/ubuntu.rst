=================
Ubuntu 源使用帮助
=================

地址
====

https://mirrors.nju.edu.cn/ubuntu/

说明
====

Ubuntu 软件源

收录架构
========

AMD64 (x86_64), Intel x86

其他架构请参考 :doc:`ubuntu-ports`

收录版本
========

所有 Ubuntu 当前支持的版本，包括开发版，具体版本见 https://wiki.ubuntu.com/Releases

对于 Ubuntu 不再支持的版本，请参考 :doc:`ubuntu-old-releases`

::

    List of releases                
                    
    Current             
                    
    Version Code name   Docs    Release date    End of Life date
    Ubuntu 17.10    Artful Aardvark Rel 19-Oct-17   Jul-18
    Ubuntu 16.04.3 LTS  Xenial Xerus    Changes 3-Aug-17    Apr-21
    Ubuntu 16.04.2 LTS  Xenial Xerus    Changes 16-Feb-17   Apr-21
    Ubuntu 16.04.1 LTS  Xenial Xerus    Changes 21-Jul-16   Apr-21
    Ubuntu 16.04 LTS    Xenial Xerus    Rel 21-Apr-16   Apr-21
    Ubuntu 14.04.5 LTS  Trusty Tahr Changes 4-Aug-16    Apr-19
    Ubuntu 14.04.4 LTS  Trusty Tahr Changes 18-Feb-16   HWE August 2016
    Ubuntu 14.04.3 LTS  Trusty Tahr Changes 6-Aug-15    HWE August 2016
    Ubuntu 14.04.2 LTS  Trusty Tahr Changes 20-Feb-15   HWE August 2016
    Ubuntu 14.04.1 LTS  Trusty Tahr Changes 24-Jul-14   Apr-19
    Ubuntu 14.04 LTS    Trusty Tahr Rel 17-Apr-14   Apr-19
                    
    Release announcements are posted on the ubuntu-announce mailing list.               
                    
    Future              
                    
    Version Code name   Docs    Release date    End of Life date
    Ubuntu 18.04 LTS    Bionic Beaver       Apr-18  
                    
    End of Life             
                    
    Version Code name   Docs    Release date    End of Life date
    Ubuntu 17.04    Zesty Zapus Rel 13-Apr-17   13-Jan-18
    Ubuntu 16.10    Yakkety Yak Rel 13-Oct-16   20-Jul-17
    Ubuntu 15.10    Wily Werewolf   Rel 22-Oct-15   28-Jul-16
    Ubuntu 15.04    Vivid Vervet    Rel 23-Apr-15   4-Feb-16
    Ubuntu 14.10    Utopic Unicorn  Rel 23-Oct-14   23-Jul-15
    Ubuntu 13.10    Saucy Salamander    Rel 17-Oct-13   17-Jul-14
    Ubuntu 13.04    Raring Ringtail Rel 25-Apr-13   27-Jan-14
    Ubuntu 12.10    Quantal Quetzal Tech / Rel  18-Oct-12   16-May-14
    Ubuntu 12.04.5 LTS  Precise Pangolin    Rel 7-Aug-14    28-Apr-17
    Ubuntu 12.04.4 LTS  Precise Pangolin    Changes 6-Feb-14    HWE August 8, 2014
    Ubuntu 12.04.3 LTS  Precise Pangolin    Changes 23-Aug-13   HWE August 8, 2014
    Ubuntu 12.04.2 LTS  Precise Pangolin    Changes 14-Feb-13   HWE August 8, 2014
    Ubuntu 12.04.1 LTS  Precise Pangolin    Changes 24-Aug-12   28-Apr-17
    Ubuntu 12.04 LTS    Precise Pangolin    Tech / Rel  26-Apr-12   28-Apr-17
    Ubuntu 11.10    Oneiric Ocelot  Tech / Rel  13-Oct-11   9-May-13
    Ubuntu 11.04    Natty Narwhal   Tech / Rel  28-Apr-11   28-Oct-12
    Ubuntu 10.10    Maverick Meerkat    Tech / Rel  10-Oct-10   10-Apr-12
    Ubuntu 10.04.4 LTS  Lucid Lynx  Changes 16-Feb-12   May 9, 2013 (Desktop)
                    April 30, 2015 (Server)
    Ubuntu 10.04.3 LTS  Lucid Lynx  Changes 21-Jul-11   
    Ubuntu 10.04.2 LTS  Lucid Lynx  Changes 18-Feb-11   
    Ubuntu 10.04.1 LTS  Lucid Lynx  Changes 17-Aug-10   
    Ubuntu 10.04 LTS    Lucid Lynx  Tech / Rel  29-Apr-10   
    Ubuntu 10.04    Lucid Lynx (Desktop)    Changes 16-Feb-12   9-May-13
    Ubuntu 9.10 Karmic Koala    Tech / Rel  29-Oct-09   30-Apr-11
    Ubuntu 9.04 Jaunty Jackalope    Tech / Rel  23-Apr-09   23-Oct-10
    Ubuntu 8.10 Intrepid Ibex   Rel 30-Oct-08   30-Apr-10
    Ubuntu 8.04.4 LTS   Hardy Heron (Server)    Changes 28-Jan-10   9-May-13
    Ubuntu 8.04.3 LTS   Hardy Heron Changes 16-Jul-09   
    Ubuntu 8.04.2 LTS   Hardy Heron Changes 22-Jan-09   
    Ubuntu 8.04.1 LTS   Hardy Heron Hardy Heron 3-Jul-08    
    Ubuntu 8.04 LTS Hardy Heron Hardy Heron/Rel 24-Apr-08   
    Ubuntu 8.04 Hardy Heron (Desktop)   Rel 24-Apr-08   12-May-11
    Ubuntu 7.10 Gutsy Gibbon    Rel 18-Oct-07   April 18th, 2009
    Ubuntu 7.04 Feisty Fawn Rel 19-Apr-07   19-Oct-08
    Ubuntu 6.10 Edgy Eft        26-Oct-06   26-Apr-08
    Ubuntu 6.06.2 LTS   Dapper Drake (Server)       21-Jan-08   1-Jun-11
    Ubuntu 6.06.1 LTS   Dapper Drake        10-Aug-06   
    Ubuntu 6.06 LTS Dapper Drake    Rel 1-Jun-06    
    Ubuntu 6.06 Dapper Drake (Desktop)  Rel 1-Jun-06    14-Jul-09
    Ubuntu 5.10 Breezy Badger   Rel 12-Oct-05   13-Apr-07
    Ubuntu 5.04 Hoary Hedgehog      8-Apr-05    31-Oct-06
    Ubuntu 4.10 Warty Warthog       26-Oct-04   30-Apr-06


使用说明
========


手动更改配置文件
----------------

.. warning::
    操作前请做好相应备份

一般情况下，将 :file:`/etc/apt/sources.list` 文件中 Ubuntu 默认的源地址 ``http://archive.ubuntu.com/``
替换为 ``http://mirrors.nju.edu.cn`` 即可。

可以使用如下命令：

::

  sudo sed -i 's/archive.ubuntu.com/mirrors.nju.edu.cn/g' /etc/apt/sources.list

.. tip::
    如果你在安装时选择的语言不是英语，默认的源地址通常不是 ``http://archive.ubuntu.com/`` ，
    而是 ``http://<country-code>.archive.ubuntu.com/ubuntu/`` ，如 ``http://cn.archive.ubuntu.com/ubuntu/`` ，
    此时只需将上面的命令进行相应的替换即可，即
    ``sudo sed -i 's/cn.archive.ubuntu.com/mirrors.nju.edu.cn/g' /etc/apt/sources.list`` 。

当然也可以直接编辑 :file:`/etc/apt/sources.list` 文件（需要使用 sudo）。以下是 Ubuntu 16.04 参考配置内容：

::

    # 默认注释了源码仓库，如有需要可自行取消注释
    deb https://mirrors.nju.edu.cn/ubuntu/ xenial main restricted universe multiverse
    # deb-src https://mirrors.nju.edu.cn/ubuntu/ xenial main restricted universe multiverse
    deb https://mirrors.nju.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse
    # deb-src https://mirrors.nju.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse
    deb https://mirrors.nju.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
    # deb-src https://mirrors.nju.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
    deb https://mirrors.nju.edu.cn/ubuntu/ xenial-security main restricted universe multiverse
    # deb-src https://mirrors.nju.edu.cn/ubuntu/ xenial-security main restricted universe multiverse

    # 预发布软件源，不建议启用
    # deb https://mirrors.nju.edu.cn/ubuntu/ xenial-proposed main restricted universe multiverse
    # deb-src https://mirrors.nju.edu.cn/ubuntu/ xenial-proposed main restricted universe multiverse

更改完 :file:`sources.list` 文件后请运行 ``sudo apt-get update`` 更新索引以生效。

.. tip::
    使用 HTTPS 可以有效避免国内运营商的缓存劫持。


镜像下载
--------

如果需要下载 Ubuntu 的 ISO 镜像以便安装，请参考 :doc:`ubuntu-releases`

相关链接
========

:官方主页: https://www.ubuntu.com/
:文档: https://help.ubuntu.com/
:Wiki: https://wiki.ubuntu.com/
:邮件列表: https://community.ubuntu.com/contribute/support/mailinglists/
:提问: https://askubuntu.com/
:论坛: https://ubuntuforums.org/
:中文论坛: https://forum.ubuntu.org.cn/
