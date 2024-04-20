# Homebrew 源使用帮助

## 地址

<https://mirrors.ustc.edu.cn/brew.git/>

## 说明

Homebrew 源代码仓库

## 使用说明

替换 USTC 镜像：

    export HOMEBREW_BREW_GIT_REMOTE="https://mirrors.ustc.edu.cn/brew.git"
    brew update

:::: note
::: title
Note
:::

若用户设置了环境变量 `HOMEBREW_BREW_GIT_REMOTE`，则每次运行
`brew update` 时将会自动设置远程。 推荐用户将环境变量
`HOMEBREW_BREW_GIT_REMOTE` 加入 shell 的 profile 设置中。

    # 对于 bash 用户
    echo 'export HOMEBREW_BREW_GIT_REMOTE="https://mirrors.ustc.edu.cn/brew.git"' >> ~/.bash_profile

    # 对于 zsh 用户
    echo 'export HOMEBREW_BREW_GIT_REMOTE="https://mirrors.ustc.edu.cn/brew.git"' >> ~/.zshrc
::::

重置为官方地址：

    unset HOMEBREW_BREW_GIT_REMOTE
    git -C "$(brew --repo)" remote set-url origin https://github.com/Homebrew/brew

:::: note
::: title
Note
:::

重置回默认远程后，用户应该删除 shell 的 profile 设置中的环境变量
`HOMEBREW_BREW_GIT_REMOTE` 以免运行 `brew update` 时远程再次被更换。

若之前使用的 `git config url.<URL>.insteadOf URL`
的方式设置的镜像，请手动删除 `config` 文件（一般为 `~/.gitconfig`
或仓库目录下的 `.git/config`）中的对应字段。
::::

## 使用科大源安装 Homebrew / Linuxbrew

首先在命令行运行如下几条命令设置环境变量：

    export HOMEBREW_BREW_GIT_REMOTE="https://mirrors.ustc.edu.cn/brew.git"
    export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.ustc.edu.cn/homebrew-core.git"
    export HOMEBREW_BOTTLE_DOMAIN="https://mirrors.ustc.edu.cn/homebrew-bottles"
    export HOMEBREW_API_DOMAIN="https://mirrors.ustc.edu.cn/homebrew-bottles/api"

之后在命令行运行 Homebrew 安装脚本：

    /bin/bash -c "$(curl -fsSL https://github.com/Homebrew/install/raw/HEAD/install.sh)"

:::: note
::: title
Note
:::

初次安装 Homebrew / Linuxbrew 时，如果无法下载安装脚本，
可以使用我们每日同步的安装脚本文件。

    /bin/bash -c "$(curl -fsSL https://mirrors.ustc.edu.cn/misc/brew-install.sh)"
::::

## 相关镜像

-   `homebrew-bottles`{.interpreted-text role="doc"}
-   `homebrew-core.git`{.interpreted-text role="doc"}
-   `homebrew-cask.git`{.interpreted-text role="doc"}
-   `homebrew-cask-versions.git`{.interpreted-text role="doc"}
-   `homebrew-services.git`{.interpreted-text role="doc"}

## 相关链接

官方主页

:   <http://brew.sh/>

brew 文档

:   <http://docs.brew.sh/>
