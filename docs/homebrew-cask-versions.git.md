# Homebrew Cask Versions 源使用帮助

## 地址

<https://mirrors.ustc.edu.cn/homebrew-cask-versions.git/>

## 说明

Homebrew cask 其他版本 (alternative versions)
软件仓库，提供使用人数多的、需要的版本不在 cask 仓库中的应用。

## 使用说明

使用 USTC 镜像安装，或将已安装的仓库远程替换为 USTC 镜像：

    brew tap --custom-remote --force-auto-update homebrew/cask-versions https://mirrors.ustc.edu.cn/homebrew-cask-versions.git

:::: note
::: title
Note
:::

若出现 `Error: invalid option: --custom-remote` 错误，请先运行
`brew update` 将 `brew` 更新至 3.2.17 或以上版本。
::::

重置为官方地址：

    brew tap --custom-remote --force-auto-update homebrew/cask-versions https://github.com/Homebrew/homebrew-cask-versions

## 相关镜像

-   `brew.git`{.interpreted-text role="doc"}
-   `homebrew-bottles`{.interpreted-text role="doc"}
-   `homebrew-core.git`{.interpreted-text role="doc"}
-   `homebrew-cask.git`{.interpreted-text role="doc"}
-   `homebrew-services.git`{.interpreted-text role="doc"}

## 相关链接

官方主页

:   <https://github.com/Homebrew/homebrew-cask-versions>

Homebrew

:   <https://brew.sh/>
