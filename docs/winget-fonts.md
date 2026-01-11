# WinGet 字体

!!! warning "测试阶段"

    截至 2026 年 1 月，WinGet 字体管理功能尚未达到普遍可用（generally available）状态，也暂未开放社区贡献，详情见 <https://github.com/microsoft/winget-pkgs/issues/300661>。本镜像当前仅供测试验证，以下内容可能发生变化。

## 地址

<https://mirrors.ustc.edu.cn/winget-fonts>

## 说明

用于字体的 WinGet（Windows 包管理器) 社区存储库

## 使用说明

!!! note

    修改 WinGet 软件源需要管理员权限，请以管理员身份运行终端。对于已[启用 `sudo`](https://learn.microsoft.com/windows/advanced-settings/sudo/#how-to-enable-sudo-for-windows) 的 Windows 11 用户，也可以使用 `sudo` 进行提权。

用以下命令替换 `winget-font` 源：

    winget source remove winget-font
    winget source add winget-font https://mirrors.ustc.edu.cn/winget-fonts --trust-level trusted

重置为官方地址：

    winget source reset winget-font

## 相关镜像

- [winget-source](winget-source.md)

## 相关链接

GitHub

:   <https://github.com/microsoft/winget-cli>

Microsoft Store

:   <https://apps.microsoft.com/store/detail/%E5%BA%94%E7%94%A8%E5%AE%89%E8%A3%85%E7%A8%8B%E5%BA%8F/9NBLGGH4NNS1>

软件源仓库

:   <https://github.com/microsoft/winget-pkgs>
