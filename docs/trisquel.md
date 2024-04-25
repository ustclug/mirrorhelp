---
trisquel_releases:
  - version: 11
    codename: aramo
  - version: 10
    codename: nabia
  - version: 9
    codename: etiona
  - version: 8
    codename: flidas
---

# Trisquel

## 地址

<https://mirrors.ustc.edu.cn/trisquel/>

## 说明

Trisquel GNU/Linux 软件源。

## 收录架构

Trisquel 支持的所有架构。

## 收录版本

所有 Trisquel 当前支持的版本

## 使用说明

!!! warning

    操作前请做好相应备份.

Trisquel 使用 APT 软件包管理系统，故其软件源使用方法与 Ubuntu 或 Debian
等很相似。

编辑 `/etc/apt/sources.list` 文件 (需要使用 sudo), 在文件最前面添加以下条目：

{% for release in trisquel_releases %}
=== "Trisquel {{ release.version }}"

    ```debsources title="/etc/apt/sources.list"
    # 默认注释了源码仓库，如有需要可自行取消注释
    deb https://mirrors.ustc.edu.cn/trisquel/ {{ release.codename }} main
    #deb-src https://mirrors.ustc.edu.cn/trisquel/ {{ release.codename }} main
    deb https://mirrors.ustc.edu.cn/trisquel/ {{ release.codename }}-security main
    #deb-src https://mirrors.ustc.edu.cn/trisquel/ {{ release.codename }}-security main
    deb https://mirrors.ustc.edu.cn/trisquel/ {{ release.codename }}-updates main
    #deb-src https://mirrors.ustc.edu.cn/trisquel/ {{ release.codename }}-updates main
    deb https://mirrors.ustc.edu.cn/trisquel/ {{ release.codename }}-backports main
    #deb-src https://mirrors.ustc.edu.cn/trisquel/ {{ release.codename }}-backports main
    ```
{% endfor %}

## 相关链接

官方主页

:   <https://trisquel.info/en>

文档

:   <https://trisquel.info/en/wiki/documentation>
