# Fedora

## 地址

<https://mirrors.ustc.edu.cn/fedora/>

## 说明

Fedora 软件源

## 收录架构

x86_64

## 收录版本

所有仍在支持的版本

## 使用说明

:::: warning
::: title
Warning
:::

操作前请做好相应备份。
::::

用以下命令替换 `/etc/yum.repos.d`{.interpreted-text role="file"}
下的文件

    sudo sed -e 's|^metalink=|#metalink=|g' \
             -e 's|^#baseurl=http://download.example/pub/fedora/linux|baseurl=https://mirrors.ustc.edu.cn/fedora|g' \
             -i.bak \
             /etc/yum.repos.d/fedora.repo \
             /etc/yum.repos.d/fedora-modular.repo \
             /etc/yum.repos.d/fedora-updates.repo \
             /etc/yum.repos.d/fedora-updates-modular.repo

:::: note
::: title
Note
:::

Fedora 39 起 modular 仓库已经不复存在（详见
[https://fedoraproject.org/wiki/Changes/RetireModularity\\](https://fedoraproject.org/wiki/Changes/RetireModularity\)
）。 因此 Fedora 39 及以上的版本不需要修改
`fedora-modular.repo`{.interpreted-text role="file"} 和
`fedora-updates-modular.repo`{.interpreted-text role="file"}。
::::

或者直接复制以下文件：

`/etc/yum.repos.d/fedora.repo`{.interpreted-text role="file"} 文件：

::: literalinclude
includes/fedora.repo
:::

`/etc/yum.repos.d/fedora-updates.repo`{.interpreted-text role="file"}
文件：

::: literalinclude
includes/fedora-updates.repo
:::

`/etc/yum.repos.d/fedora-modular.repo`{.interpreted-text role="file"}
文件：

::: literalinclude
includes/fedora-modular.repo
:::

`/etc/yum.repos.d/fedora-updates-modular.repo`{.interpreted-text
role="file"} 文件：

::: literalinclude
includes/fedora-updates-modular.repo
:::

最后运行 `sudo dnf makecache` 生成缓存。

## 相关链接

官方主页

:   <https://getfedora.org/>

邮件列表

:   <https://fedoraproject.org/wiki/Communicating_and_getting_help>

论坛

:   <https://forums.fedoraforum.org/>

文档

:   <https://docs.fedoraproject.org/>

Wiki

:   <https://fedoraproject.org/wiki/>

镜像列表

:   <https://admin.fedoraproject.org/mirrormanager>
