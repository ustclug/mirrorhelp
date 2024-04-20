# Gentoo Portage

## 地址

<https://mirrors.ustc.edu.cn/gentoo-portage>

## 说明

Gentoo Portage Ebuild 源（Rsync 方式同步）

## 收录架构

ALL

## 使用说明

新建或修改 `/etc/portage/repos.conf/gentoo.conf`
 ：

    [DEFAULT]
    main-repo = gentoo

    [gentoo]
    location = /usr/portage
    sync-type = rsync
    sync-uri = rsync://rsync.mirrors.ustc.edu.cn/gentoo-portage
    auto-sync = yes

## 相关镜像

-   `gentoo`
-   `gentoo.git`

## 相关链接

官方主页

:   <https://www.gentoo.org/>

邮件列表

:   <https://www.gentoo.org/main/en/lists.xml>

论坛

:   <https://forums.gentoo.org/>

文档

:   <https://www.gentoo.org/doc/en/>

Wiki

:   <https://wiki.gentoo.org/>

镜像列表

:   <https://www.gentoo.org/main/en/mirrors-rsync.xml>
