============================
Infinality-bundle 源使用帮助
============================

地址
====

https://mirrors.ustc.edu.cn/infinality-bundle/

说明
====

Infinality-bundle 软件、字体源

使用说明
========

请在 :file:`/etc/pacman.conf` 里根据需要添加：

::

    [infinality-bundle]
    Server = https://mirrors.ustc.edu.cn/infinality-bundle/$arch

    [infinality-bundle-multilib]
    Server = https://mirrors.ustc.edu.cn/infinality-bundle/multilib/$arch

    [infinality-bundle-fonts]
    Server = https://mirrors.ustc.edu.cn/infinality-bundle/fonts

在更新之前，请先执行以下命令导入公钥

::

    # pacman-key -r 962DDE58
    # pacman-key --lsign-key 962DDE58
    # pacman -Syy

相关链接
========

:官方主页: https://bohoomil.com/
:ArchWiki: `<https://wiki.archlinux.org/index.php/Infinality_(简体中文)>`_
