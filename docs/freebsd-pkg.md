# FreeBSD pkg

## 地址

<https://mirrors.ustc.edu.cn/freebsd-pkg/>

## 说明

FreeBSD 预编译软件包镜像

## 收录架构

所有受官方支持的架构，当前稳定版 FreeBSD 13 支持的架构包括 amd64, i386,
aarch64。

## 收录版本

自 FreeBSD 11 以后的版本，包括 quarterly 和滚动更新的 latest 仓库。

FreeBSD 9 以前的版本不支持新的 pkg 包管理器（pkgng），请升级到新版。

## 使用方法

FreeBSD pkg 包管理器的官方源配置是
`/etc/pkg/FreeBSD.conf`{.interpreted-text role="file"}
，请先检查该文件内容。注意其中的 `url`
参数配置了官方仓库的地址，我们需要把它替换为镜像站的地址。

该配置文件是 FreeBSD 基本系统的一部分，会随着 `freebsd-update`
更新，请不要直接修改，而是创建
`/usr/local/etc/pkg/repos/FreeBSD.conf`{.interpreted-text role="file"}
覆盖配置，文件内容如下：

    FreeBSD: {
      url: "http://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/quarterly",
    }

如果要使用滚动更新的 latest 仓库，把 `url` 配置最后的 `quarterly` 换成
`latest` 即可。

修改配置后，运行 `pkg update -f` 更新索引。

!!! tip

    使用 HTTPS 可以有效避免国内运营商的缓存劫持，但需要事先安装
    `security/ca_root_nss` 软件包。

## 相关链接

官方主页

:   <https://www.freebsd.org>

论坛

:   <https://forums.freebsd.org>

文档

:   <https://www.freebsd.org/doc>
