===================
Julia 镜像使用帮助
===================

.. role:: sh(code)
   :language: bash

地址
====

https://mirrors.ustc.edu.cn/julia/

说明
====

此镜像包括 Julia 的官方包注册表 `General <https://github.com/JuliaRegistries/General>`_ 以及装包时所涉及的源代码和二进制依赖。

关于 Julia 二进制程序的镜像，请在 `Julia Releases <https://mirrors.ustc.edu.cn/julia-releases/>`_ 下载。

注：本镜像的使用需要 Julia :sh:`v1.4.0` 或更新的版本。

使用说明
--------

只需要设置环境变量 :sh:`JULIA_PKG_SERVER` 即可切换镜像。若成功切换镜像，则能通过 :sh:`versioninfo()` 查询到相关信息，例如：

.. code-block:: julia

    julia> versioninfo()
    Julia Version 1.4.1
    Commit 381693d3df* (2020-04-14 17:20 UTC)
    Platform Info:
    OS: Linux (x86_64-pc-linux-gnu)
    CPU: Intel(R) Core(TM) i7-6800K CPU @ 3.40GHz
    WORD_SIZE: 64
    LIBM: libopenlibm
    LLVM: libLLVM-8.0.1 (ORCJIT, broadwell)
    Environment:
    JULIA_PKG_SERVER = https://mirrors.ustc.edu.cn/julia

若不设置该环境变量则默认使用官方服务器 :sh:`https://pkg.julialang.org` 作为上游。


临时使用
--------

不同系统和命令行下设置环境变量的方式各不相同，在命令行下可以通过以下方式来临时修改环境变量

* Linux Bash\: :sh:`export JULIA_PKG_SERVER=https://mirrors.ustc.edu.cn/julia`
* Windows Powershell\: :sh:`$env:JULIA_PKG_SERVER = 'https://mirrors.ustc.edu.cn/julia'`

也可以利用 JuliaCN 社区维护的中文本地化工具包 `JuliaZH <https://github.com/JuliaCN/JuliaZH.jl>`_ 来进行切换：

.. code-block:: julia

    using JuliaZH # 在 using 时会自动切换到国内的镜像站
    JuliaZH.set_mirror("USTC") # 也可以选择手动切换到 BFSU 镜像
    JuliaZH.mirrors # 查询记录的上游信息


永久使用
--------

不同系统和命令行下永久设定环境变量的方式也不相同，例如 Linux Bash 下可以通过修改 :sh:`~/.bashrc` 文件实现该目的：

.. code-block:: text

    # ~/.bashrc
    export JULIA_PKG_SERVER=https://mirrors.ustc.edu.cn/julia

此外， 这里再提供一种针对 Julia 的全平台通用的方式： :sh:`$JULIA_DEPOT_PATH/config/startup.jl` (默认为
:sh:`~/.julia/config/startup.jl` ) 文件定义了每次启动 Julia 时都会执行的命令， 编辑该文件，
添加以下内容即可：

.. code-block:: text

    # ~/.julia/config/startup.jl
    ENV["JULIA_PKG_SERVER"] = "https://mirrors.ustc.edu.cn/julia"

也可以选择使用 :sh:`JuliaZH` 来一键修改/创建 :sh:`startup.jl` 文件：

.. code-block:: julia

    julia> JuliaZH.generate_startup("default")
    ┌ Info: 添加 PkgServer
    │   服务器地址 = "https://pkg.julialang.org"
    └   配置文件 = "/root/.julia/config"

    julia> JuliaZH.generate_startup("USTC")
    ┌ Info: 更新 PkgServer
    │   原服务器地址 = "https://pkg.julialang.org"
    │   新服务器地址 = "https://mirrors.USTC.edu.cn/julia"
    └   配置文件 = "/root/.julia/config"


若要临时禁止，可以通过 :sh:`julia --startup-file=no` 来取消执行 :sh:`startup.jl` 文件。


常见问题
========


为什么有些包的下载还是很慢？
--------------------------------

有两类数据不会被镜像：

* 在 :sh:`deps/build.jl` 文件中硬编码的下载地址，例如 `GR <https://github.com/jheinen/GR.jl/blob/70f025d5cb439d036409f1985107cb5e1615097f/deps/build.jl#L116>`_.
* 在 :sh:`Artifacts.toml` 中没有给出 :sh:`download` 项的资源, 例如 `TestImages <https://github.com/JuliaImages/TestImages.jl/blob/eaa94348df619c65956e8cfb0032ecddb7a29d3a/Artifacts.toml>`_.

在安装包含这两类数据的包时，其数据依然是从原始地址进行下载，因此若网络不稳定则可能会在 `build` 阶段报错。

为什么注册表还是从原地址下载？
--------------------------------

Julia :sh:`v1.4.0` 之前的版本采用的是 :sh:`git clone` 的方式拉取注册表。为了保持兼容性，如果现有的注册表是一个完整的 git 仓库的话，
那么即使设置了 PkgServer 作为上游镜像也依然会通过 :sh:`git` 来进行更新，换句话说，不会通过镜像站来下载注册表数据。

以默认注册表 :sh:`General` 为例，只需要手动将其重置到镜像站即可：

1. 删除当前注册表： :sh:`(@v1.4) pkg> registry rm General`
2. 从镜像站下载/拉取注册表： :sh:`(@v1.4) pkg> registry add General` -- 将无法在旧 Julia 版本中更新注册表

为什么有些包还是从原地址下载？
--------------------------------

镜像站只镜像注册表中记录的包，因此如果某些包是通过指定 URL 的方式来安装的话，那么该包的更新不会从镜像站进行下载。
这常见于那些还未注册的包及其版本，例如：

.. code-block:: julia

    ]add Flux#master
    ]add https://github.com/FluxML/Flux.jl.git
    Pkg.add(PackageSpec(url="https://github.com/FluxML/Flux.jl.git"))


加快 Conda.jl 相关操作的速度
--------------------------------

Conda.jl 的加速分为两部分：

- :sh:`conda` 的安装：如果系统中没有找到 :sh:`conda` 的话， :sh:`Conda.jl` 会下载并安装一份
  :sh:`miniconda`。 如果这一步下载非常缓慢的话，你可以提前从 `BFSU镜像站 <https://mirrors.bfsu.edu.cn/help/anaconda/>`_ 下载并安装 :sh:`anaconda`， 然后通过设置环境变量 
  :sh:`CONDA_JL_HOME=$HOME/anaconda3` 来指定 :sh:`Conda.jl` 所使用的conda， 这样就避免重复下载 miniconda.
  （:sh:`\$HOME/anaconda3` 是 anaconda3 的默认安装位置， 你可能需要根据具体情况进行调整。）

- :sh:`conda add` 等操作的加速： 这个只需要配置 anaconda 镜像源即可，即修改 :sh:`~/.condarc` 文
  件。 具体的配置可以查看镜像站中 anaconda 镜像的使用说明。
