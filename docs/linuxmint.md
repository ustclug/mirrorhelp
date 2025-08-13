# Linux Mint

## 地址

<https://mirrors.ustc.edu.cn/linuxmint/>

## 说明

Linux Mint 软件源

## 收录架构

i386，amd64

## 收录版本

- 所有 Linux Mint 发行版本
- 所有 LMDE 发行版本

## 使用方法

!!! warning

    操作前请做好相应备份。

!!! tip

    Linux Mint 也与 Ubuntu 和 Debian 类似，都采用 apt 作为包管理器。`/etc/apt/sources.list.d/official-package-repositories.list` 中包含了来自 Ubuntu 或 Debian 的源，以及 Linux Mint 的源。对于来自 Ubuntu 与 Debian 的部分源，可以参考 [Ubuntu 帮助](https://mirrors.ustc.edu.cn/help/ubuntu.html)与 [Debian 帮助](https://mirrors.ustc.edu.cn/help/debian.html)进行修改。Ubuntu 与 Debian 的发行版代号应保持不变。比如系统原来是 `bookworm` (Debian 12)，不可更改为 `trixie` (Debian 13)。更改代号会破坏依赖。

需要修改 `/etc/apt/sources.list.d/official-package-repositories.list`（注意备份），把 `packages.linuxmint.com` 替换为镜像源。其中 Linux Mint 的部分如下：

{% for release in linuxmint_releases %}

=== "{{ release.version }}"

    ```debsources title="/etc/apt/sources.list.d/official-package-repositories.list"
    deb http://mirrors.ustc.edu.cn/linuxmint {{ release.codename }} main upstream import backport
    ```

{% endfor %}

替换基于 Ubuntu 的镜像源:

```shell
sudo sed -i 's@//.*archive.ubuntu.com@//mirrors.ustc.edu.cn@g' /etc/apt/sources.list.d/official-package-repositories.list
```

替换基于 Debian (LMDE) 的镜像源:

```shell
sudo sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
```

然后运行 `sudo apt-get update` 更新索引以生效。

!!! tip

    完成后请不要再使用 mintsources（自带的图形化软件源设置工具）进行任何操作，因为在操作后，无论是否有按"确定"，mintsources 均会覆盖 `/etc/apt/sources.list.d/official-package-repositories.list`。

    目前 Linux Mint 暂未使用 DEB822 格式进行分发。如果您需要自行更改为 DEB822 格式，请参考下面的格式进行手动修改。

--8<-- "deb822.md"

## 相关链接

官方主页

:   <https://www.linuxmint.com/>

论坛

:   <https://forums.linuxmint.com/index.php>

文档

:   <https://linuxmint.com/documentation.php>
