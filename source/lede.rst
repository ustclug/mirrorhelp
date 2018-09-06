=======================
OpenWRT/LEDE 源使用帮助
=======================

地址
====

https://mirrors.ustc.edu.cn/lede/

说明
====

OpenWRT/LEDE 下载站镜像。

这是对 https://downloads.lede-project.org/ 的完整镜像，内容包括官方支持的平台的 ROM、SDK 及工具链、软件仓库镜像等。

使用说明
========

一般情况下，下载来自 ``downloads.lede-project.org`` 的文件时，将 URL 中的这部分域名替换为 ``mirrors.ustc.edu.cn/lede`` 即可。

如要使用本镜像作为 OpenWRT/LEDE 系统 opkg 软件仓库，SSH 登录路由器编辑 :file:`/etc/opkg/distfeeds.conf` 文件，同样按照上面的方法替换域名即可。可以使用如下命令操作：

::

    sed -i 's_downloads\.lede-project\.org_mirrors.ustc.edu.cn/lede_' /etc/opkg/distfeeds.conf

之后运行 `opkg update` 更新软件索引，注意检查是否出现错误。

相关链接
========

:官方主页: https://openwrt.org/
:LEDE 项目论坛: https://forum.lede-project.org/
:OpenWRT 论坛: https://forum.openwrt.org/
