# FreeBSD pkg

## 地址

[https://mirrors.ustc.edu.cn/freebsd-pkg/](https://mirrors.ustc.edu.cn/freebsd-pkg/)

## 说明

FreeBSD 预编译软件包（pkg）镜像。

## 收录架构与版本

收录所有受 FreeBSD 官方支持版本的 amd64 与 aarch64 架构，具体支持情况请参见
[https://pkg.freebsd.org/](https://pkg.freebsd.org/)。

仓库包含季度分支 quarterly 以及滚动更新的 latest。

!!! tip

```
并非所有版本与架构同时提供 quarterly 或 latest 仓库，例如 CURRENT 仅提供 latest。
```

## 使用方法

!!! warning

```
在进行任何配置修改前，请自行做好相应备份。
```

为了避免潜在的向后兼容问题，FreeBSD 基本系统中并未预置完整的 pkg(8) 工具，需要通过网络安装。
相关说明请参见 [man pkg(7)](https://man.freebsd.org/cgi/man.cgi?query=pkg)。

安装方式为直接执行命令 `pkg` 并按提示确认安装。
为避免因网络问题导致安装失败，建议**先配置镜像源后再安装 pkg**。

### 配置镜像源

FreeBSD pkg 官方源的默认配置文件路径为：

```
/etc/pkg/FreeBSD.conf
```

**不建议直接修改该文件**。该文件属于 FreeBSD 基本系统的一部分，可能会随系统更新而发生变化。

推荐通过覆盖配置的方式，在以下路径创建文件：

```
/usr/local/etc/pkg/repos/USTC.conf
```

文件内容示例如下：

```yaml
ustc: {
  url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/quarterly"
}

FreeBSD-ports: { enabled: no }
```

!!! important

```
自 FreeBSD 15 起，pkg 默认仓库名已由 `FreeBSD` 更名为 `FreeBSD-ports`。  
若仍使用 `FreeBSD: { enabled: no }`，将**无法真正禁用官方源**。
```

若需要使用滚动更新的 latest 仓库，只需将 `url` 中的 `quarterly` 替换为 `latest`。

配置完成后，执行以下命令强制更新索引：

```
pkg update -f
```

!!! tip

```
若未启用 [pkgbase](https://wiki.freebsd.org/pkgbase)，pkg 仅用于管理第三方软件（Ports 对应的二进制包），不会更新基本系统。  
基本系统与 pkg 安装的软件相互独立，互不影响。
```

## 相关链接

官方主页
:   [https://www.freebsd.org](https://www.freebsd.org)

邮件列表
:   [https://www.freebsd.org/community/mailinglists](https://www.freebsd.org/community/mailinglists)

论坛
:   [https://forums.freebsd.org](https://forums.freebsd.org)

文档
:   [https://docs.freebsd.org](https://docs.freebsd.org)

Wiki
:   [https://wiki.freebsd.org](https://wiki.freebsd.org)

官方 Discord
:   [https://discord.com/invite/freebsd](https://discord.com/invite/freebsd)
