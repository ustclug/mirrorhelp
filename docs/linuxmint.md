# Linux Mint

## 地址

<https://mirrors.ustc.edu.cn/linuxmint/>

## 说明

Linux Mint 软件源

## 收录架构

i386，amd64

## 收录版本

-   所有 Linux Mint 发行版本
-   所有 LMDE 发行版本

## 使用方法

:::: warning
::: title
Warning
:::

操作前请做好相应备份。
::::

编辑
`/etc/apt/sources.list.d/official-package-repositories.list`{.interpreted-text
role="file"} ：

-   对于基于 Ubuntu 的原版，以 Linuxmint 19 为例：

```{=html}
<!-- -->
```
    deb https://mirrors.ustc.edu.cn/linuxmint/ tara main upstream import backport 
    deb https://mirrors.ustc.edu.cn/ubuntu/ bionic main restricted universe multiverse
    deb https://mirrors.ustc.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
    deb https://mirrors.ustc.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
    deb https://mirrors.ustc.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
    deb http://archive.canonical.com/ubuntu/ bionic partner

-   对于基于 Debian 的 LMDE，以 LMDE 2 为例：

```{=html}
<!-- -->
```
    deb https://mirrors.ustc.edu.cn/linuxmint/ betsy main upstream import
    deb https://mirrors.ustc.edu.cn/debian jessie main contrib non-free
    deb https://mirrors.ustc.edu.cn/debian jessie-updates main contrib non-free
    deb https://mirrors.ustc.edu.cn/debian jessie-backports main contrib non-free
    deb https://mirrors.ustc.edu.cn/debian-security/ jessie/updates main non-free contrib
    deb https://mirrors.ustc.edu.cn/deb-multimedia/ jessie main non-free

然后运行 `sudo apt-get update` 更新索引以生效。

:::: tip
::: title
Tip
:::

完成后请不要再使用
mintsources（自带的图形化软件源设置工具）进行任何操作，因为在操作后，无论是否有按"确定"，mintsources
均会复写
`/etc/apt/sources.list.d/official-package-repositories.list`{.interpreted-text
role="file"} 。
::::

## 相关链接

官方主页

:   <https://www.linuxmint.com/>

论坛

:   <https://forums.linuxmint.com/index.php>

文档

:   <https://linuxmint.com/documentation.php>
