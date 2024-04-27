# Debian Security

## 地址

<https://mirrors.ustc.edu.cn/debian-security/>

## 说明

Debian 软件安全更新源

## 收录架构

Debian 支持的所有架构，如 AMD64 (x86_64), Intel x86, ARM, MIPS, ppc64el,
s390x 等

## 收录版本

Debian Old Old Stable, Old Stable, Stable

当前 Stable 为 Debian 12，代号为 Bookworm

## 使用说明

!!! warning

    操作前请做好相应备份

!!! warning "安全更新源注意事项"

    由于镜像站同步安全更新存在延迟，可能导致安全更新无法及时获取，因此仅建议在确实有需要的情况下才使用镜像站的安全更新源。

一般情况下，将 `/etc/apt/sources.list` 或 `/etc/apt/sources.list.d/debian.sources` 文件中 Debian 默认的源地址 `http://security.debian.org/debian-security/`（或 `http://deb.debian.org/debian-security/`）替换为 `http://mirrors.ustc.edu.cn/debian-security/` 即可。

--8<-- "deb822.md"

!!! note

    从 Debian 11 "Bullseye" 开始，安全更新仓库名从 `发行版代号/updates`
    更新为 `发行版代号-security`，详见 [Debian 11 (bullseye) 发行说明](https://www.debian.org/releases/bullseye/amd64/release-notes/ch-information.zh-cn.html#security-archive)，请旧版本用户注意。

可以直接使用如下命令完成上述修改：

=== "`sources.list` 格式"

    ```shell
    sudo sed -i 's/security.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
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
        deb http://mirrors.ustc.edu.cn/debian-security/ {{ debian_security }} {{ debian_components }}
        # deb-src http://mirrors.ustc.edu.cn/debian-security/ {{ debian_security }} {{ debian_components }}
        ```

    === "DEB822 格式"

        ```yaml title="/etc/apt/sources.list.d/debian.sources"
        Types: deb
        URIs: http://mirrors.ustc.edu.cn/debian-security
        Suites: {{ debian_security }}
        Components: {{ debian_components }}
        Signed-By: /usr/share/keyrings/debian-archive-keyring.gpg
        ```

        如果需要使用源码仓库，可以在 Types 中添加 `deb-src`。

        如果需要使用 backports 软件源，可以在 Suites 中添加 `{{ release.codename }}-backports`。

{% endfor %}

更改后请运行 `sudo apt-get update` 更新索引以生效。

!!! tip

    使用 HTTPS 可以有效避免国内运营商的缓存劫持。

另外，也可以使用 snullp 大叔开发的 [配置生成器](https://mirrors.ustc.edu.cn/repogen)。

## 相关链接

官方主页

:   <https://www.debian.org/security/>

Debian 安全追踪网

:   <https://security-tracker.debian.org/tracker/>
