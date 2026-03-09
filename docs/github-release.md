# GitHub Release

## 地址

<https://mirrors.ustc.edu.cn/github-release/>

## 说明

部分 GitHub 仓库 Release 内容的镜像

## 收录仓库

仅镜像最新版本：

- [3-manifolds/Sage_macOS](https://github.com/3-manifolds/Sage_macOS)
- [adoptium/temurin8-binaries](https://github.com/adoptium/temurin8-binaries)
- [adoptium/temurin11-binaries](https://github.com/adoptium/temurin11-binaries)
- [adoptium/temurin17-binaries](https://github.com/adoptium/temurin17-binaries)
- [adoptium/temurin21-binaries](https://github.com/adoptium/temurin21-binaries)
- [astral-sh/python-build-standalone](https://github.com/astral-sh/python-build-standalone)
- [astral-sh/uv](https://github.com/astral-sh/uv)
- [coder/code-server](https://github.com/coder/code-server)
- [conda-forge/miniforge](https://github.com/conda-forge/miniforge)
- [deepmodeling/deepmd-kit](https://github.com/deepmodeling/deepmd-kit)
- [git-for-windows/git](https://github.com/git-for-windows/git)
- [Homebrew/homebrew-portable-ruby](https://github.com/Homebrew/homebrew-portable-ruby)
- [Homebrew/glibc-bootstrap](https://github.com/Homebrew/glibc-bootstrap)
- [pbatard/rufus](https://github.com/pbatard/rufus)
- [typst/typst](https://github.com/typst/typst)
- [ungoogled-software/ungoogled-chromium-windows](https://github.com/ungoogled-software/ungoogled-chromium-windows)
- [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver)

镜像最新的两个版本：

- [TheThirdOne/rars](https://github.com/TheThirdOne/rars)

镜像最新的五个版本：

- [XmacsLabs/mogan](https://github.com/XmacsLabs/mogan)

## 使用说明

一般情况下，直接前往此镜像地址，点击即可进行下载。

### python-build-standalone

可配置以下环境变量：

```sh
UV_PYTHON_INSTALL_MIRROR=https://mirrors.ustc.edu.cn/github-release/astral-sh/python-build-standalone/
```

需要注意的是，我们仅镜像了最新的一个 release，并且排除了符合以下正则的文件：

- debug.+full
- ppc64le
- s390x
- i686

服务端不存在的文件会被重定向到 GitHub 官方仓库。

## 相关链接

Adoptium 官网

:   <https://adoptium.net/>

Rufus 官网

:   <https://rufus.ie/>
