# GHCup

## 地址

<https://mirrors.ustc.edu.cn/ghcup/>

## 说明

GHCup 类似 Rustup，可以用于安装 Haskell 工具链。建议搭配 Hackage 和
Stackage 源使用。

!!! warning

    当前的 GHCup 0.0.8 版本会在安装时也尝试安装 cabal，因此建议在安装 GHCup 前先手动配置 cabal 使用镜像，方法为参考文档 [hackage](https://mirrors.ustc.edu.cn/help/hackage.html#cabal) 中的说明，修改 `~/.cabal/config`。

## 使用方法

参考如下步骤可安装完整的 Haskell 工具链。

!!! note

    以下命令会安装并配置 GHCup 0.0.8 版本的元数据。可查看
    <https://mirrors.ustc.edu.cn/ghcup/ghcup-metadata/>
    目录的内容，并选择需要安装的 GHCup 版本的 yaml 文件替换以下命令中的
    URL。

**第一步（可选）** ：使用科大源安装 GHCup 本体。如已经安装 GHCup，可跳到下一步。

Linux, FreeBSD, macOS 用户
: &#32;
    ```bash
    # 在终端中运行如下命令
    curl --proto '=https' --tlsv1.2 -sSf https://mirrors.ustc.edu.cn/ghcup/sh/bootstrap-haskell | BOOTSTRAP_HASKELL_YAML=https://mirrors.ustc.edu.cn/ghcup/ghcup-metadata/ghcup-0.0.8.yaml sh
    ```    
Windows 用户
: &#32;
    ```bash
    # 以非管理员身份在 PowerShell 中运行如下命令
    $env:BOOTSTRAP_HASKELL_YAML = 'https://mirrors.ustc.edu.cn/ghcup/ghcup-metadata/ghcup-0.0.8.yaml'
    Set-ExecutionPolicy Bypass -Scope Process -Force;[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072;Invoke-Command -ScriptBlock ([ScriptBlock]::Create((Invoke-WebRequest https://mirrors.ustc.edu.cn/ghcup/sh/bootstrap-haskell.ps1 -UseBasicParsing))) -ArgumentList $true
    ```

**第二步** ：配置 GHCup 使用科大源。编辑 `~/.ghcup/config.yaml` 增加如下配置：

    url-source:
      OwnSource: 
        - https://mirrors.ustc.edu.cn/ghcup/ghcup-metadata/ghcup-0.0.8.yaml

**第三步（可选）** ：配置 Cabal 和 Stack 使用科大源，请参考文档 [hackage](hackage.md) 和 [stackage](stackage.md)。

!!! warning

    科大 GHCup 源仅支持较新的 GHCup 版本（元数据格式版本仅支持 0.0.6
    及以上）。如果你使用的 GHCup 版本比较旧，请参考上述步骤安装新版本
    GHCup。

## 非正式频道

Ghcup 提供预发布版本（`prereleases`）、交叉编译版本（`cross`）和基础安装版本（`vanilla`）作为额外频道。要启用这些频道，修改 `~/.ghcup/config.yaml` 中的 `url-source` 节，并依需要添加不同的频道对应的元数据。

    url-source:
      OwnSource:
        - https://mirrors.ustc.edu.cn/ghcup/ghcup-metadata/ghcup-0.0.8.yaml
        - https://mirrors.ustc.edu.cn/ghcup/ghcup-metadata/ghcup-prereleases-0.0.8.yaml
        - https://mirrors.ustc.edu.cn/ghcup/ghcup-metadata/ghcup-cross-0.0.8.yaml
        - https://mirrors.ustc.edu.cn/ghcup/ghcup-metadata/ghcup-vanilla-0.0.8.yaml

关于使用 GHCup 安装交叉编译器的说明，请参考 GHCup User Guide 的 [Cross Support](https://www.haskell.org/ghcup/guide/#cross-support) 章节。

## 相关链接

Haskell 主页

:   <https://www.haskell.org/>

GHCup 主页

:   <https://www.haskell.org/ghcup/>
