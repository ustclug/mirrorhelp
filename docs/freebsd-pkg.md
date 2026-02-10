# FreeBSD pkg

## 地址

<https://mirrors.ustc.edu.cn/freebsd-pkg/>

## 说明

FreeBSD 预编译软件包的**动态缓存**

## 收录架构与版本

所有受官方支持版本的 amd64 和 aarch64 架构，详细参见 <https://pkg.freebsd.org/>。

仓库包括季度分支 quarterly 和滚动更新的 latest 仓库。

!!! tip

    并非所有版本和架构都同时拥有 quarterly 或 latest 仓库，如 CURRENT 仅有 latest。

## 使用方法

!!! warning

    在操作前请做好相应备份。

为了避免可能出现的向后兼容问题，基本系统中未预置真实的 pkg(8) 工具，需要在线安装。参见 [man pkg(7)](https://man.freebsd.org/cgi/man.cgi?query=pkg)。安装方法为直接输入命令 `pkg` 根据提示进行确认安装。为了避免因网络问题造成安装失败，建议先按以下方法换源后再安装 pkg。

FreeBSD pkg 包管理器的官方源的配置路径为 `/etc/pkg/FreeBSD.conf`。不建议直接修改此文件：该配置文件是 FreeBSD 基本系统的一部分，会随着基本系统的更新而变化。

应创建路径及文件 `/usr/local/etc/pkg/repos/USTC.conf` 来覆盖配置，文件内容如下：

=== "FreeBSD 16"

    === "`latest` 分支"

        ```yaml
        ustc: { 
            url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/latest"
        }
        FreeBSD-ports: { enabled: no }
        ```

=== "FreeBSD 15"

    === "`quarterly` 分支"

        ```yaml
        ustc: { 
            url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/quarterly"
        }
        FreeBSD-ports: { enabled: no }
        ```

    === "`latest` 分支"

        ```yaml
        ustc: { 
            url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/latest"
        }
        FreeBSD-ports: { enabled: no }
        ```

=== "FreeBSD 14"

    === "`quarterly` 分支"

        ```yaml
        ustc: { 
            url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/quarterly"
        }
        FreeBSD: { enabled: no }
        ```

    === "`latest` 分支"

        ```yaml
        ustc: { 
            url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/latest"
        }
        FreeBSD: { enabled: no }
        ```

修改配置后，运行 `pkg update -f` 更新索引。

!!! tip

    如未配置 [pkgbase](https://wiki.freebsd.org/pkgbase)，则 pkg 仅管理用户安装的第三方软件（Port），无法更新基本系统。基本系统与通过 pkg 安装的软件互不干涉。

## 相关链接

官方主页

:   <https://www.freebsd.org>

邮件列表

:   <https://www.freebsd.org/community/mailinglists>

论坛

:   <https://forums.freebsd.org>

文档

:   <https://docs.freebsd.org>

Wiki

:   <https://wiki.freebsd.org>

官方 Discord

:   <https://discord.com/invite/freebsd>
