========================
Manjaro Linux 源使用帮助
========================

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

Manjaro 提供了 pacman-mirrors 脚本，一般情况下，当 pacman-mirrorlist 被升级后，Manjaro 会马上运行 ``pacman-mirrors -g`` 自动写入软件源列表。这样做不但会耗掉较多的时间，而且还会覆盖原先的 :file:`/etc/pacman.d/mirrorlist` 。因此我们不推荐你直接编辑 :file:`/etc/pacman.d/mirrorlist` 。

一个较好的解决方法是：

创建一个名为 :file:`/etc/pacman.d/mirrors/Custom` 的文件，并在里面加入：

::

  ##
  ## Pacman Mirrorlist
  ##

  [Custom]
  Server = https://mirrors.ustc.edu.cn/manjaro/$branch/$repo/$arch
  # 可以加入其它的软件源，格式与这个类似。
  
保存后接着编辑 :file:`/etc/pacman-mirrors.conf` ，使 pacman-mirrors 只对这个文件列出的镜像站进行排行：

::

  OnlyCountry=Custom
  
当然如果你不希望 pacman-mirrors 按连接速度排序而是希望它能直接将这个文件里的镜像站按先后顺序拷贝到 :file:`/etc/pacman.d/mirrorlist` ，你可以进一步修改：

::
    
    Method=random

最后使用 pacman-mirrors 手动生成 :file:`/etc/pacman.d/mirrorlist` ：

::

  sudo pacman-mirrors -g

相关链接
========

:官方主页: https://www.manjaro.org/
:邮件列表: https://lists.manjaro.org/mailman/listinfo
:论坛: https://forum.manjaro.org/
:Wiki: https://wiki.manjaro.org/
