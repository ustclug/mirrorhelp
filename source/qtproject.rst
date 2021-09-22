===============
Qt 镜像使用帮助
===============

在线安装
--------

从
http://mirrors.ustc.edu.cn/qtproject/official_releases/online_installers/
下载在线安装器。

可以使用以下两种方式之一在安装器中配置使用科大源下载 Qt：

1. （推荐）新版本的安装器（4.0.1-1 后）支持 ``--mirror`` 命令行参数。在命令行中执行安装器，添加 ``--mirror https://mirrors.ustc.edu.cn/qtproject`` 参数。例如 Windows 下执行当前目录的安装器的命令为 ``.\qt-unified-windows-x86-online.exe --mirror https://mirrors.ustc.edu.cn/qtproject``；
2. 或在启动安装器后在设置中禁用默认源，添加新源 http://mirrors.ustc.edu.cn/qtproject/online/qtsdkrepository/linux_x64/root/qt/ （其他版本注意更改地址）。
