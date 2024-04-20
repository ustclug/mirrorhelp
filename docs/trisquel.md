# Trisquel

## 地址

<https://mirrors.ustc.edu.cn/trisquel/>

## 说明

Trisquel GNU/Linux 软件源.

## 收录架构

Trisquel 支持的所有架构.

## 收录版本

所有 Trisquel 当前支持的版本

## 使用说明

:::: warning
::: title
Warning
:::

操作前请做好相应备份.
::::

Trisquel 使用 APT 软件包管理系统，故其软件源使用方法与 Ubuntu 或 Debian
等很相似。

以 Flidas 为例, 编辑 `/etc/apt/sources.list`{.interpreted-text
role="file"} 文件 (需要使用 sudo), 在文件最前面添加以下条目:

    deb https://mirrors.ustc.edu.cn/trisquel/ flidas main
    deb-src https://mirrors.ustc.edu.cn/trisquel/ flidas main
    deb https://mirrors.ustc.edu.cn/trisquel/ flidas-security main
    deb-src https://mirrors.ustc.edu.cn/trisquel/ flidas-security main
    deb https://mirrors.ustc.edu.cn/trisquel/ flidas-updates main
    deb-src https://mirrors.ustc.edu.cn/trisquel/ flidas-updates main
    deb https://mirrors.ustc.edu.cn/trisquel/ flidas-backports main
    deb-src https://mirrors.ustc.edu.cn/trisquel/ flidas-backports main

## 相关链接

官方主页

:   <https://trisquel.info/en>

文档

:   <https://trisquel.info/en/wiki/documentation>
