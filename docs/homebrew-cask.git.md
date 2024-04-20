# Homebrew Cask

## 地址

<https://mirrors.ustc.edu.cn/homebrew-cask.git/>

## 说明

Homebrew cask 软件仓库，提供 macOS 应用和大型二进制文件

## 使用说明

!!! note

    Brew 4.0 版本后默认使用元数据 JSON API
    获取仓库信息，因此在大部分情况下都不再需要进行如下配置。可参考
    `homebrew-bottles` 进行相关配置。

使用 USTC 镜像安装，或将已安装的仓库远程替换为 USTC 镜像：

    brew tap --custom-remote --force-auto-update homebrew/cask https://mirrors.ustc.edu.cn/homebrew-cask.git

!!! note

    若出现 `Error: invalid option: --custom-remote` 错误，请先运行
    `brew update` 将 `brew` 更新至 3.2.17 或以上版本。

重置为官方地址：

    brew tap --custom-remote --force-auto-update homebrew/cask https://github.com/Homebrew/homebrew-cask

!!! note

    Caskroom 的 Git 地址在 2018 年 5 月 25 日从
    <https://github.com/caskroom/homebrew-cask> 迁移到了
    <https://github.com/Homebrew/homebrew-cask>。

## 相关镜像

-   `brew.git`
-   `homebrew-bottles`
-   `homebrew-core.git`
-   `homebrew-cask-versions.git`
-   `homebrew-services.git`

## 相关链接

官方主页

:   <https://caskroom.github.io>

Homebrew

:   <https://brew.sh/>
