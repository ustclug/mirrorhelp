# OpenWrt

## 地址

<https://mirrors.ustc.edu.cn/openwrt/>

## 说明

OpenWrt 下载站镜像。

这是对 <https://downloads.openwrt.org/> 的除了 snapshots 与预发布版本（RC）以外的完整镜像，内容包括官方支持的平台的 ROM、SDK 及工具链、软件仓库镜像等。

!!! tip

    访问 snapshots 与 RC 版本内容会重定向至反向代理，如果需要下载相关文件，务必使用 HTTPS，否则连接可能会被中断。

!!! tip

    访问 <https://mirrors.ustc.edu.cn/lede/> 会被自动重定向到 <https://mirrors.ustc.edu.cn/openwrt/>。

## 使用说明

一般情况下，下载来自 `downloads.openwrt.org` 的文件时，将 URL 中的这部分域名替换为 `mirrors.ustc.edu.cn/openwrt` 即可。

如要使用本镜像作为 OpenWrt 系统 opkg 软件仓库，SSH 登录路由器编辑 `/etc/opkg/distfeeds.conf` 文件，同样按照上面的方法替换域名即可。可以使用如下命令操作：

```shell
sed -i 's/downloads.openwrt.org/mirrors.ustc.edu.cn\/openwrt/g' /etc/opkg/distfeeds.conf
```

之后运行 `opkg update` 更新软件索引，注意检查是否出现错误。

!!! tip

    使用 HTTPS 可以有效避免国内运营商的缓存劫持，但需要另行安装 `libustream-openssl ca-bundle ca-certificates`。

## 相关链接

官方主页

:   <https://openwrt.org/>

OpenWRT 文档

:   <https://openwrt.org/docs/start>

OpenWRT 论坛

:   <https://forum.openwrt.org/>
