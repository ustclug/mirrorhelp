=======================
openSUSE 源使用帮助
=======================

地址
====

https://mirrors.ustc.edu.cn/opensuse/

说明
====

openSUSE 软件源

收录架构
========

i586, x86_64

使用说明
========

手动配置软件源
-------------

.. warning::
以下配置方法适用于从未自行配置软件源的用户，其他用户请根据具体情况自行配置 ，以下仅供参考。

禁用原有软件源；

::

  sudo zypper mr -da

添加科大镜像源，以 openSUSE Leap 42.2 为例；

::

  sudo zypper ar -fc https://mirrors.ustc.edu.cn/opensuse/distribution/leap/42.2/repo/oss USTC:42.2:OSS
  sudo zypper ar -fc https://mirrors.ustc.edu.cn/opensuse/distribution/leap/42.2/repo/non-oss USTC:42.2:NON-OSS
  sudo zypper ar -fc https://mirrors.ustc.edu.cn/opensuse/update/leap/42.2/oss USTC:42.2:UPDATE-OSS
  sudo zypper ar -fc https://mirrors.ustc.edu.cn/opensuse/update/leap/42.2/non-oss USTC:42.2:UPDATE-NON-OSS

命令中最后一个参数为每一个源指定了一个 alias （别称），可以根据个人喜好更改。

手动刷新软件源

::

  sudo zypper ref

(2)图形界面下配置方法

以 openSUSE 13.2 为例：

#. 打开 YaST；
#. 点击 Software 分组中的 Software Repositories；
#. 在打开的窗口上方的列表中点击 openSUSE-13.2-Oss ，点击 Edit；
#. 将 download.opensuse.org 替换为 mirrors.ustc.edu.cn/opensuse，点OK；
#. 再用同样的方法编辑 openSUSE-13.2-Non-Oss 和 openSUSE-13.2-Update。

注意事项
========

* 由于使用了 MirrorBrain 技术， 中央服务器 (download.opensuse.org) 会按照 IP 地理位置中转下载请求到附近的 镜像服务器（但刷新软件源时仍从中央服务器获取元数据），所以更改软件源通常 只会加快刷新软件源的速度，而对下载速度影响不大。参见 openSUSE 中文论坛。
* 我们不提供 source 和 debug 源。
* Tumbleweed 滚动发行版软件源的地址与上述例子稍有不同。

相关链接
========

:官方主页: https://www.opensuse.org/
:邮件列表: https://en.opensuse.org/Communicate/Mailinglists
:论坛: https://forums.opensuse.org/
:中文论坛: https://forum.suse.org.cn/
:Wiki: https://en.opensuse.org/
:中文 Wiki: https://zh.opensuse.org/
:文档: https://en.opensuse.org/Documentation
:openSUSE Guide: https://lug.ustc.edu.cn/sites/opensuse-guide/
