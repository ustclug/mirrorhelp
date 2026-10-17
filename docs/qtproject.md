# Qt

## 地址

<https://mirrors.ustc.edu.cn/qtproject/>

## 说明

Qt 应用开发框架目前支持的版本。已经不再被官方维护的版本未同步。

## 安装

!!! warning "校外使用官方安装器的限制"

    根据 [Qt 镜像仓库调整通知](https://servers.ustclug.org/2026/10/qt-adjustments/)，本站将取消对 Qt 官方安装器 User-Agent 的特殊放行规则。校外使用官方安装器访问本站时可能受到拦截，仅设置 `--mirror` 无法解决此问题。可以使用下文介绍的 Qit，或参考 [TUNA issue 中的 mitmproxy 方案](https://github.com/tuna/issues/issues/1936#issuecomment-2737251530)。

    **校内访问没有 User-Agent 限制，可以继续使用官方安装器。**

### 使用 Qit

[Qit](https://github.com/taoky/qit) 是使用 GTK 编写的第三方 Qt 安装器，无需登录 Qt 账号，并使用明确的 User-Agent 标识下载请求。

从 [Qit 最新版本镜像目录](https://mirrors.ustc.edu.cn/github-release/taoky/qit/LatestRelease/) 下载适合操作系统和 CPU 架构的安装包。文件名中的版本号以目录中实际提供的为准；`x86_64` 对应常见的 Intel / AMD 64 位电脑，`aarch64` 对应 ARM64。

| 操作系统 | 文件名格式 | 启动方式 |
| --- | --- | --- |
| Windows | `Qit-<版本>-windows-<架构>.zip` | 解压后运行其中的 `qit.exe` |
| Linux | `Qit-<版本>-linux-<架构>.AppImage` | 添加可执行权限后运行 |
| macOS | `Qit-<版本>-darwin-<架构>.dmg` | 打开磁盘映像，直接运行其中的 Qit；Apple Silicon 选择 `aarch64` |

Linux 启动示例（请替换为实际下载的文件名）：

```console
chmod +x Qit-0.1.2-linux-x86_64.AppImage
./Qit-0.1.2-linux-x86_64.AppImage
```

#### 图形界面使用

1. 在「设置」中选择镜像站。
2. 进入「安装 Qt」，选择目标、Qt 版本、开发套件及需要的组件，并确认安装目录。
3. 点击「下一步」，检查组件列表、下载大小和许可证后开始安装。
4. 安装完成后，可在「已安装」中查看安装记录、获取环境配置说明或卸载。

#### 命令行使用

Qit 安装包中也包含 `qit-cli`。Windows 下在解压后的目录中运行 `.\qit-cli.exe`；macOS 下在终端进入挂载后的磁盘映像目录，运行 `./Qit.app/Contents/MacOS/qit-cli`。

Linux 可直接通过 AppImage 的 `--cli` 参数启动命令行工具（文件名按实际版本和架构调整）：

```sh
chmod +x Qit-0.1.2-linux-x86_64.AppImage
./Qit-0.1.2-linux-x86_64.AppImage --cli --help
```

如果在容器等没有可用 FUSE 的环境中运行，提示无法挂载 AppImage，可在 `--cli` 前添加 `--appimage-extract-and-run`，由 AppImage 自动解包并运行：

```sh
./Qit-0.1.2-linux-x86_64.AppImage --appimage-extract-and-run --cli --help
```

下文的其他命令也需要同样添加此参数。

以下以 Linux x86_64 的桌面 Qt 为例。默认使用教育网联合镜像站。如果需要指定本镜像站，需添加 `--mirror https://mirrors.ustc.edu.cn/qtproject/` 参数。

先查询可用的版本仓库：

```sh
qit-cli repositories
```

`repositories` 默认查询当前主机平台的 `desktop` 仓库，也可通过 `--host` 和 `--target` 指定平台和目标。根据输出的仓库路径查询组件，例如：

```sh
qit-cli packages --repo online/qtsdkrepository/linux_x64/desktop/qt6_681/
```

这里的 Qt 6.8.1 仓库路径和下文的组件 ID 仅作示例，请以当前镜像的查询结果为准，其他操作系统和架构也需要使用对应的仓库与组件。选择组件后，先用 `plan` 查看包含依赖的安装计划及许可证：

```sh
qit-cli plan --repo online/qtsdkrepository/linux_x64/desktop/qt6_681/ \
    qt.qt6.681.linux_gcc_64
```

确认接受相关许可证后执行安装。以下命令将安装到 `$HOME/Qit/qt-6.8.1`；Windows 用户请将 `--root` 的值改为所需路径，例如 `C:\Qit`。

```sh
qit-cli install --repo online/qtsdkrepository/linux_x64/desktop/qt6_681/ \
    --root "$HOME/Qit" --name qt-6.8.1 --accept-licenses \
    qt.qt6.681.linux_gcc_64
```

可以在命令末尾指定多个组件 ID，也可以重复 `--repo` 参数加载多个仓库。向已有的 Qit 安装添加组件时，在 `install` 命令中加上 `--add-components`，使用相同的 `--root` 和 `--name`，并指定要添加的组件 ID。

查看已安装记录：

```sh
qit-cli list
```

需要卸载时，使用 `list` 输出中的安装 ID（将 `INSTALLATION_ID` 替换为实际值）：

```sh
qit-cli uninstall INSTALLATION_ID --yes
```

命令结果以 JSON 输出到标准输出，进度和错误输出到标准错误；添加全局参数 `--json` 可使进度信息也以 JSON 输出。更多参数可通过 `qit-cli <子命令> --help` 查看。

### 使用官方安装器

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
