# FreeBSD pkg

## 地址

<https://mirrors.ustc.edu.cn/freebsd-pkg/>

## 说明

FreeBSD 预编译软件包的**动态缓存**

## 收录架构与版本

所有受官方支持版本的 amd64 和 aarch64 架构，详细参见 <https://pkg.freebsd.org/>。

仓库提供两种软件包分支：季度更新的 quarterly 与滚动更新的 latest。两者仅影响第三方软件包（ports）。

!!! tip

    软件包分支与 FreeBSD 基本系统版本无关。不同 RELEASE / STABLE / CURRENT 均可使用 quarterly 或 latest。

    但并非所有版本和架构都同时提供两种分支，例如 CURRENT 通常仅提供 latest。

    从 FreeBSD 15.0 起，若在安装系统时或事后手动启用了 pkgbase，则基本系统组件也会以软件包形式由 pkg 管理。此时，`/usr/local/etc/pkg/repos`目录下将会默认带有一个配置文件。

    在这种情况下，请先检查 `/usr/local/etc/pkg/repos` 是否为空，并确认 `/usr/local/etc/pkg` 下不存在旧配置文件；如存在请先备份。

    请勿将文件命名为其他 `.conf` 以外的名称，避免覆盖现有设置。
    
    完成确认后，再写入对应的镜像配置到 `/usr/local/etc/pkg/repos/ustc.conf`。

## 使用方法

!!! warning

    在操作前请做好相应备份。

    此处只列出了 `quaterly` 季度分支，若有其他需求，请自行修改。

    为了避免可能出现的向后兼容问题，基本系统中未预置真实的 pkg(8) 工具，需要在线安装。参见 [man pkg(7)](https://man.freebsd.org/cgi/man.cgi?query=pkg)。安装方法为直接输入命令 `pkg` 根据提示进行确认安装。为了避免因网络问题造成安装失败，建议先按以下方法换源后再安装 pkg。

    FreeBSD pkg 包管理器的官方源的配置路径为 `/etc/pkg/FreeBSD.conf`。不建议直接修改此文件：该配置文件是 FreeBSD 基本系统的一部分，会随着基本系统的更新而变化。
    应新创建路径及文件 `/usr/local/etc/pkg/repos/ustc.conf` 来覆盖配置，文件内容如下：

=== "FreeBSD 15.X-RELEASE"

    ```yaml
    ustc-ports: { 
        url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/quarterly",
        mirror_type: "none",
        signature_type: "fingerprints",
        fingerprints: "/usr/share/keys/pkg",
        enabled: yes
    }

    ustc-ports-kmods: {
        url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/kmods_quarterly_${VERSION_MINOR}",
        mirror_type: "none",
        signature_type: "fingerprints",
        fingerprints: "/usr/share/keys/pkg",
        enabled: yes
    }

    FreeBSD-ports: { 
        enabled: no 
    }

    FreeBSD-ports-kmods: { 
        enabled: no 
    }

    # 仅当启用 pkgbase 时才添加以下内容
    #ustc-base: {
    #   url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/base_release_${VERSION_MINOR}",
    #   mirror_type: "none",
    #   signature_type: "fingerprints",
    #   fingerprints: "/usr/share/keys/pkgbase-${VERSION_MAJOR}",
    #   enabled: yes
    #}

    #FreeBSD-base: {
    #   enabled: no
    #}
    ```

=== "FreeBSD 14.X-RELEASE"

    ```yaml
    ustc: { 
        url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/quarterly",
        mirror_type: "none",
        signature_type: "fingerprints",
        fingerprints: "/usr/share/keys/pkg",
        enabled: yes
    }

    ustc-kmods: {
        url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/kmods_quarterly_${VERSION_MINOR}",
        mirror_type: "none",
        signature_type: "fingerprints",
        fingerprints: "/usr/share/keys/pkg",
        enabled: yes
    }

    FreeBSD: { 
        enabled: no 
    }

    FreeBSD-kmods: { 
        enabled: no 
    }
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
