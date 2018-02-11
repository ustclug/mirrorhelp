========================
Manjaro Linux 源使用帮助
========================

地址
====

https://mirrors.nju.edu.cn/manjaro/

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

生成可用中国镜像站列表：

::

  sudo pacman-mirrors -i -c China -m rank
        
勾选 ``http://mirrors.nju.edu.cn/manjaro/`` ，然后按 ``OK`` 键两次。
        
最后刷新缓存：

::

  sudo pacman -Syy

相关链接
========

:官方主页: https://www.manjaro.org/
:邮件列表: https://lists.manjaro.org/mailman/listinfo
:论坛: https://forum.manjaro.org/
:Wiki: https://wiki.manjaro.org/
