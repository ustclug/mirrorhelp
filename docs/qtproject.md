# Qt

## 地址

<https://mirrors.ustc.edu.cn/qtproject/>

## 说明

Qt 应用开发框架目前支持的版本。已经不再被官方维护的版本未同步。

## 安装

首先，从 <https://mirrors.ustc.edu.cn/qtproject/official_releases/online_installers/> 下载在线安装器。然后可以使用以下两种方式之一在安装器中配置使用科大源下载 Qt：

1. （**推荐**）目前安装器支持 `--mirror` 命令行参数。在命令行中执行安装器，添加 `--mirror https://mirrors.ustc.edu.cn/qtproject` 参数即可。

    Windows 下执行当前目录的安装器的命令为：

    ```console
    .\qt-unified-windows-x86-online.exe --mirror https://mirrors.ustc.edu.cn/qtproject
    ```

    Linux (amd64)：

    ```console
    chmod +x qt-unified-linux-x64-online.run
    ./qt-unified-linux-x64-online.run --mirror https://mirrors.ustc.edu.cn/qtproject
    ```

    Linux (aarch64)：

    ```console
    chmod +x qt-unified-linux-arm64-online.run
    ./qt-unified-linux-arm64-online.run --mirror https://mirrors.ustc.edu.cn/qtproject
    ```

    macOS 需要点击 dmg 挂载后，使用终端打开挂载后的 dmg 目录：

    ```console
    # 文件名需要根据实际情况调整
    open qt-unified-macOS-x64-4.7.0-online.app --args --mirror https://mirrors.ustc.edu.cn/qtproject
    ```

2. （不建议）在启动安装器后在设置中禁用默认源，添加新源
    <http://mirrors.ustc.edu.cn/qtproject/online/qtsdkrepository/linux_x64/root/qt/>
    （其他版本注意更改地址）。
