==================
GHCup 源使用帮助
==================

地址
====

https://mirrors.ustc.edu.cn/ghcup/

说明
====

GHCup 类似 Rustup，可以用于安装 Haskell 工具链。建议搭配 Hackage 和 Stackage 源使用。

使用方法
========

参考如下步骤可安装完整的 Haskell 工具链。

.. note::

   以下命令会安装并配置 GHCup 0.0.7 版本的元数据。
   可查看 https://mirrors.ustc.edu.cn/ghcup/ghcup-metadata/ 目录的内容，并选择需要安装的 GHCup 版本的 yaml 文件替换以下命令中的 URL。

**第一步（可选）** ：使用科大源安装 GHCup 本体。如已经安装 GHCup，可跳到下一步。

::

   # Linux, FreeBSD, macOS 用户：在终端中运行如下命令
   curl --proto '=https' --tlsv1.2 -sSf https://mirrors.ustc.edu.cn/ghcup/sh/bootstrap-haskell | BOOTSTRAP_HASKELL_YAML=https://mirrors.ustc.edu.cn/ghcup/ghcup-metadata/ghcup-0.0.7.yaml sh

   # Windows 用户：以非管理员身份在 PowerShell 中运行如下命令
   $env:BOOTSTRAP_HASKELL_YAML = 'https://mirrors.ustc.edu.cn/ghcup/ghcup-metadata/ghcup-0.0.7.yaml'
   Set-ExecutionPolicy Bypass -Scope Process -Force;[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072;Invoke-Command -ScriptBlock ([ScriptBlock]::Create((Invoke-WebRequest https://mirrors.ustc.edu.cn/ghcup/sh/bootstrap-haskell.ps1 -UseBasicParsing))) -ArgumentList $true

**第二步** ：配置 GHCup 使用科大源。编辑 ``~/.ghcup/config.yaml`` 增加如下配置：

::

   url-source:
       OwnSource: https://mirrors.ustc.edu.cn/ghcup/ghcup-metadata/ghcup-0.0.7.yaml

**第三步（可选）** ：配置 Cabal 和 Stack 使用科大源，请参考文档 :doc:`hackage` 和 :doc:`stackage` 。

.. warning::

   科大 GHCup 源仅支持较新的 GHCup 版本（元数据格式版本仅支持 0.0.6 及以上）。如果你使用的 GHCup 版本比较旧，请参考上述步骤安装新版本 GHCup。

相关链接
========

:Haskell 主页: https://www.haskell.org/
:GHCup 主页: https://www.haskell.org/ghcup/
