========================
Arch Linux CN 源使用帮助
========================

地址
====

https://mirrors.ustc.edu.cn/archlinuxcn/

说明
====

Arch Linux CN 软件源

简介
====

Arch Linux 中文社区仓库是由 Arch Linux 中文社区驱动的非官方用户仓库。包含中文用户常用软件、工具、字体/美化包等。

仓库地址：http://repo.archlinuxcn.org

使用说明
========

在 :file:`/etc/pacman.conf` 文件末尾添加两行：

::

    [archlinuxcn]
    Server = https://mirrors.ustc.edu.cn/archlinuxcn/$arch

可以使用如下命令添加：

::

    cat >> /etc/pacman.conf <<'EOF'
    [archlinuxcn]
    Server = https://mirrors.ustc.edu.cn/archlinuxcn/$arch
    EOF

然后请安装 ``archlinuxcn-keyring`` 包以导入 GPG key。

相关链接
========

:Arch Linux 中文社区主页: https://www.archlinuxcn.org
:Arch Linux 中文社区仓库 / 镜像加速源介绍: https://www.archlinuxcn.org/archlinux-cn-repo-and-mirror/
