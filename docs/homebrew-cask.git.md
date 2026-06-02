# Homebrew Cask

## 地址

<https://mirrors.ustc.edu.cn/homebrew-cask.git/>

## 说明

Homebrew cask 软件仓库，提供 macOS 应用和大型二进制文件

## 使用说明

!!! warning

    由于 Brew 4.0 版本后默认使用元数据 JSON API 获取仓库信息，自 2026 年 6 月开始，我们不再提供此镜像，以下配置不再有效。请参考 [`homebrew-bottles`](./homebrew-bottles.md) 进行相关配置。

使用 USTC 镜像安装，或将已安装的仓库远程替换为 USTC 镜像：

```shell
brew tap --custom-remote homebrew/cask https://mirrors.ustc.edu.cn/homebrew-cask.git
```

重置为官方地址：

```shell
brew tap --custom-remote homebrew/cask https://github.com/Homebrew/homebrew-cask.git
```

!!! note

    Caskroom 的 Git 地址在 2018 年 5 月 25 日从
    <https://github.com/caskroom/homebrew-cask> 迁移到了
    <https://github.com/Homebrew/homebrew-cask>。

## 相关镜像

- [brew.git](brew.git.md)
- [homebrew-bottles](homebrew-bottles.md)

## 相关链接

官方主页

:   <https://caskroom.github.io>

Homebrew

:   <https://brew.sh/>
