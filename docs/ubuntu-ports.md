# Ubuntu Ports

## 地址

<https://mirrors.ustc.edu.cn/ubuntu-ports/>

## 说明

Ubuntu 软件源

## 收录架构

arm64, armhf, PowerPC, ppc64el, s390x

## 收录版本

所有 Ubuntu 当前对该架构支持的版本，包括开发版

对于 Ubuntu 不再支持的版本，请参考 [ubuntu-old-releases](ubuntu-old-releases.md)。

## 使用说明

### 手动更改配置文件

!!! warning

    操作前请做好相应备份

在 `/etc/apt/sources.list` 或 `/etc/apt/sources.list.d/ubuntu.sources` 文件中，将软件源的地址改为 `http://mirrors.ustc.edu.cn/ubuntu-ports`。

--8<-- "deb822.md"

可以使用如下命令：

!!! warning "安全更新源注意事项"

    因镜像站同步有延迟，可能会导致生产环境系统不能及时检查、安装上最新的安全更新，**不建议替换 security 源**。
    但是由于 Ubuntu Ports 中软件与安全更新源地址相同，因此以下提供的例子中均一并替换。

- 传统格式（`/etc/apt/sources.list`）

    ```shell
    sudo sed -i 's@//ports.ubuntu.com@//mirrors.ustc.edu.cn@g' /etc/apt/sources.list
    ```

- DEB822 格式（`/etc/apt/sources.list.d/ubuntu.sources`）

    ```shell
    sudo sed -i 's@//ports.ubuntu.com@//mirrors.ustc.edu.cn@g' /etc/apt/sources.list.d/ubuntu.sources
    ```

以下是参考配置内容，**同时修改了软件源与安全更新源**：

{% for release in ubuntu_releases %}
=== "Ubuntu {{ release.version }}"

    === "`sources.list` 格式"

        ```debsources title="/etc/apt/sources.list"
        # 默认注释了源码仓库，如有需要可自行取消注释
        deb https://mirrors.ustc.edu.cn/ubuntu-ports/ {{ release.codename }} main restricted universe multiverse
        # deb-src https://mirrors.ustc.edu.cn/ubuntu-ports/ {{ release.codename }} main restricted universe multiverse

        deb https://mirrors.ustc.edu.cn/ubuntu-ports/ {{ release.codename }}-security main restricted universe multiverse
        # deb-src https://mirrors.ustc.edu.cn/ubuntu-ports/ {{ release.codename }}-security main restricted universe multiverse

        deb https://mirrors.ustc.edu.cn/ubuntu-ports/ {{ release.codename }}-updates main restricted universe multiverse
        # deb-src https://mirrors.ustc.edu.cn/ubuntu-ports/ {{ release.codename }}-updates main restricted universe multiverse

        deb https://mirrors.ustc.edu.cn/ubuntu-ports/ {{ release.codename }}-backports main restricted universe multiverse
        # deb-src https://mirrors.ustc.edu.cn/ubuntu-ports/ {{ release.codename }}-backports main restricted universe multiverse

        # 预发布软件源，不建议启用
        # deb https://mirrors.ustc.edu.cn/ubuntu-ports/ {{ release.codename }}-proposed main restricted universe multiverse
        # deb-src https://mirrors.ustc.edu.cn/ubuntu-ports/ {{ release.codename }}-proposed main restricted universe multiverse
        ```

    === "DEB822 格式"

        ```yaml title="/etc/apt/sources.list.d/ubuntu.sources"
        Types: deb
        URIs: https://mirrors.ustc.edu.cn/ubuntu-ports
        Suites: {{ release.codename }} {{ release.codename }}-updates {{ release.codename }}-backports
        Components: main restricted universe multiverse
        Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg

        Types: deb
        URIs: https://mirrors.ustc.edu.cn/ubuntu-ports
        Suites: {{ release.codename }}-security
        Components: main universe restricted multiverse
        Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg
        ```

        如果需要使用源码仓库，可以在 Types 中添加 `deb-src`。

        如果需要使用预发布软件源，可以在 Suites 中添加 `{{ release.codename }}-proposed`。
{% endfor %}

更改后请运行 `sudo apt-get update` 更新索引以生效。

!!! tip

    使用 HTTPS 可以有效避免国内运营商的缓存劫持，但需要事先安装 `apt-transport-https`。

### 镜像下载

相关架构的 ISO 下载请参考 [ubuntu-cdimage](ubuntu-cdimage.md)。

## 相关链接

Ubuntu ARM

:   <https://wiki.ubuntu.com/ARM>

Ubuntu PowerPC

:   <https://wiki.ubuntu.com/PowerPC>

Ubuntu ppc64el

:   <https://wiki.ubuntu.com/ppc64el>

Ubuntu s390x

:   <https://wiki.ubuntu.com/S390X>
