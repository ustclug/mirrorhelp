# Debian

## 地址

<https://mirrors.ustc.edu.cn/debian/>

## 说明

Debian 软件源

## 收录架构

Debian 支持的所有架构，如 AMD64 (x86_64), Intel x86, ARM, MIPS, ppc64el, s390x 等

## 收录版本

Debian Old Old Stable, Old Stable, Stable, Testing, Unstable (sid)

{% for release in debian_releases %}
{% if loop.first %}
当前 Stable 为 Debian {{ release.version }}，代号为 {{ release.codename }}。
{% endif %}
{% endfor %}

## 使用说明

!!! warning

    操作前请做好相应备份。

一般情况下，将 `/etc/apt/sources.list` 或 `/etc/apt/sources.list.d/debian.sources` 文件中 Debian 默认的源地址 `http://deb.debian.org/` 替换为 `http://mirrors.ustc.edu.cn` 即可。

--8<-- "deb822.md"

可以使用如下命令：

=== "`sources.list` 格式"

    ```shell
    sudo sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
    ```

=== "DEB822 格式"

    ```shell
    sudo sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list.d/debian.sources
    ```

    目前使用 DEB822 格式的 Debian 分发仅有容器镜像，且其安全更新源默认设置为 `http://deb.debian.org/debian-security`，因此以上命令会同时替换 Debian 官方源和安全更新源。

当然也可以直接编辑 APT 源文件（需要使用 sudo）。以下是参考配置内容：

{% for release in debian_releases %}

{% set debian_components = "main contrib non-free" %}
{% if release.version >= 12 %}
{% set debian_components = debian_components + " non-free-firmware" %}
{% endif %}

{% set debian_security = release.codename + "-security" %}
{% if release.version < 11 %}
{% set debian_security = release.codename + "/updates" %}
{% endif %}

=== "Debian {{ release.version }}"

    === "`sources.list` 格式"

        ```debsources title="/etc/apt/sources.list"
        # 默认注释了源码仓库，如有需要可自行取消注释
        deb http://mirrors.ustc.edu.cn/debian {{ release.codename }} {{ debian_components }}
        # deb-src http://mirrors.ustc.edu.cn/debian {{ release.codename }} {{ debian_components }}
        deb http://mirrors.ustc.edu.cn/debian {{ release.codename }}-updates {{ debian_components }}
        # deb-src http://mirrors.ustc.edu.cn/debian {{ release.codename }}-updates {{ debian_components }}

        # backports 软件源，请按需启用
        # deb http://mirrors.ustc.edu.cn/debian {{ release.codename }}-backports {{ debian_components }}
        # deb-src http://mirrors.ustc.edu.cn/debian {{ release.codename }}-backports {{ debian_components }}
        ```

    === "DEB822 格式"

        ```yaml title="/etc/apt/sources.list.d/debian.sources"
        Types: deb
        URIs: http://mirrors.ustc.edu.cn/debian
        Suites: {{ release.codename }} {{ release.codename }}-updates
        Components: {{ debian_components }}
        Signed-By: /usr/share/keyrings/debian-archive-keyring.gpg

        Types: deb
        URIs: http://mirrors.ustc.edu.cn/debian-security
        Suites: {{ debian_security }}
        Components: {{ debian_components }}
        Signed-By: /usr/share/keyrings/debian-archive-keyring.gpg
        ```

        !!! warning "以上 DEB822 格式的参考配置包含了对 debian-security 源的修改"

        如果需要使用源码仓库，可以在 Types 中添加 `deb-src`。

        如果需要使用 backports 软件源，可以在 Suites 中添加 `{{ release.codename }}-backports`。

{% endfor %}

!!! tip

    从 Debian 12 (bookworm) 开始，仓库添加了非自由固件组件 `non-free-firmware`。如果正在使用 bookworm, testing 或 sid，并且需要使用非自由固件，则在编辑配置时需要添加 `non-free-firmware`。其中以上参考配置已经添加。

    详情参考 <https://wiki.debian.org/Firmware> 与
    [Debian bug #1030189](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1030189)。

同时你也可能需要更改 Debian Security（安全更新）源，请参考 [debian-security](debian-security.md)。

更改后请运行 `sudo apt-get update` 更新索引以生效。

!!! tip

    使用 HTTPS 可以有效避免国内运营商的缓存劫持。

另外，也可以使用 snullp 大叔开发的 [配置生成器](https://mirrors.ustc.edu.cn/repogen)。

## 相关链接

官方主页

:   <https://www.debian.org/>

邮件列表

:   <https://www.debian.org/MailingLists/>

Wiki

:   <https://wiki.debian.org/>

文档

:   <https://www.debian.org/doc/>

镜像列表

:   <https://www.debian.org/mirror/list>
