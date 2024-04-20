# Homebrew Core

## 地址

<https://mirrors.ustc.edu.cn/homebrew-core.git/>

## 说明

Homebrew 核心软件仓库

## 使用说明

!!! note

    Brew 4.0 版本后默认使用元数据 JSON API
    获取仓库信息，因此在大部分情况下都不再需要进行如下配置。可参考
    `homebrew-bottles` 进行相关配置。

替换 USTC 镜像：

    export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.ustc.edu.cn/homebrew-core.git"
    brew update

!!! note

    若用户设置了环境变量 `HOMEBREW_CORE_GIT_REMOTE`，则每次运行
    `brew update` 时将会自动设置远程。推荐用户将环境变量
    `HOMEBREW_CORE_GIT_REMOTE` 加入 shell 的 profile 设置中。

        # 对于 bash 用户
        echo 'export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.ustc.edu.cn/homebrew-core.git"' >> ~/.bash_profile

        # 对于 zsh 用户
        echo 'export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.ustc.edu.cn/homebrew-core.git"' >> ~/.zshrc

重置为官方地址：

    unset HOMEBREW_CORE_GIT_REMOTE
    brew tap --custom-remote homebrew/core https://github.com/Homebrew/homebrew-core

!!! note

    若出现 `Error: invalid option: --custom-remote` 错误，请先运行
    `brew update` 将 `brew` 更新至 3.2.17 或以上版本。
    重置回默认远程后，用户应该删除 shell 的 profile 设置中的环境变量
    `HOMEBREW_CORE_GIT_REMOTE` 以免运行 `brew update` 时远程再次被更换。

!!! note

    Linuxbrew 核心仓库（`linuxbrew-core`）自 2021 年 10 月 25 日（`brew`
    版本 3.3.0 起）被弃用，Linuxbrew 用户应迁移至 `homebrew-core`。
    Linuxbrew 用户请依本镜像说明重新设置镜像。注意迁移前请先运行
    `brew update` 将 `brew` 更新至 3.3.0 或以上版本。
    迁移过程中若出现任何问题，可使用如下命令重新安装 `homebrew-core`：

        export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.ustc.edu.cn/homebrew-core.git"
        rm -rf "$(brew --repo homebrew/core)"
        brew tap --custom-remote --force-auto-update homebrew/core https://mirrors.ustc.edu.cn/homebrew-core.git

## 相关镜像

- [brew.git](brew.git.md)
- [homebrew-bottles](homebrew-bottles.md)
- [homebrew-cask.git](homebrew-cask.git.md)
- [homebrew-cask-versions.git](homebrew-cask-versions.git.md)
- [homebrew-services.git](homebrew-services.git.md)

## 相关链接

官方主页

:   <http://brew.sh/>

brew 文档

:   <http://docs.brew.sh/>
