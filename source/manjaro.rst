=====================
Manjaro Linux 源使用帮助
=====================

地址
====

https://mirrors.ustc.edu.cn/manjaro/

说明
====

Manjaro Linux 软件源

收录版本
========

Stable, Testing, Unstable

收录架构
========

i686, x86_64

使用说明
========

Manjaro 提供了 pacman-mirrors 脚本，一般情况下，当 pacman-mirrorlist 被升级后，它会马上运行 ``pacman-mirrors -g`` 自动刷新软件源列表。这样做不但会耗掉较多的时间，而且还会覆盖原先的 :file:`/etc/pacman.d/mirrorlist` 。因此我们不推荐你直接编辑 :file:`/etc/pacman.d/mirrorlist` 。

一个较好的解决方法是：

创建一个名为 :file:`/etc/pacman.d/mirrors/Custom` 的文件，并在里面加入：

::

  ##
  ## Pacman Mirrorlist
  ##

  [Custom]
  Server = https://mirrors.ustc.edu.cn/manjaro/$branch/$repo/$arch
  # 可以加入其它你希望作为后备的软件源，格式与这个类似。
  
保存后接着编辑 :file:`/etc/pacman-mirrors.conf`：

::

  OnlyCountry=Custom
  
最后使用 pacman-mirrors 手动生成 :file:`/etc/pacman.d/mirrorlist` ：

::

  sudo pacman-mirrors -g

相关链接
========

:官方主页: https://www.manjaro.org/
:邮件列表: https://lists.manjaro.org/mailman/listinfo
:论坛: https://forum.manjaro.org/
:Wiki: https://wiki.manjaro.org/
