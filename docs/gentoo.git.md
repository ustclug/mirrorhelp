# Gentoo Git 源使用帮助

## 地址

<https://mirrors.ustc.edu.cn/gentoo.git>

## 说明

Gentoo Portage Ebuild 源 （Git 方式同步）

## 收录架构

ALL

## 使用说明

请确保系统中已安装 `dev-vcs/git`。

修改 `/etc/portage/repos.conf/gentoo.conf`{.interpreted-text
role="file"} 中的 `sync-type` 为 `git`，`sync-uri` 为
`https://mirrors.ustc.edu.cn/gentoo.git` 。

以下是修改后的：

    [DEFAULT]
    main-repo = gentoo

    [gentoo]
    location = /var/db/repos/gentoo
    sync-type = git
    sync-uri = https://mirrors.ustc.edu.cn/gentoo.git
    auto-sync = yes
    sync-rsync-verify-jobs = 1
    sync-rsync-verify-metamanifest = yes
    sync-rsync-verify-max-age = 24
    sync-openpgp-key-path = /usr/share/openpgp-keys/gentoo-release.asc
    sync-openpgp-keyserver = hkps://keys.gentoo.org
    sync-openpgp-key-refresh-retry-count = 40
    sync-openpgp-key-refresh-retry-overall-timeout = 1200
    sync-openpgp-key-refresh-retry-delay-exp-base = 2
    sync-openpgp-key-refresh-retry-delay-max = 60
    sync-openpgp-key-refresh-retry-delay-mult = 4
    sync-webrsync-verify-signature = yes

-   第一次使用 `Git` 同步方式的用户（从 `Rsync` 方式同步换到 `Git`
    方式同步）：

按照上述教程更改完
`/etc/portage/repos.conf/gentoo.conf`{.interpreted-text
role="file"}，需要：

    # 删除本地 main tree 目录
    rm -rf /var/db/repos/gentoo

    # 重新同步
    emerge --sync

-   已经配置过 `Git` 同步方式的用户（其他镜像站换中科大源）只需要：

更改完 `/etc/portage/repos.conf/gentoo.conf`{.interpreted-text
role="file"}：

    # 进入 main tree 目录
    cd /var/db/repos/gentoo

    # 将 remote url 设置为中科大
    git remote set-url origin https://mirrors.ustc.edu.cn/gentoo.git

    # 重新同步
    emerge --sync

## 相关镜像

-   `gentoo`{.interpreted-text role="doc"}
-   `gentoo-portage`{.interpreted-text role="doc"}

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
