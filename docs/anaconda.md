# Anaconda

## 地址

<https://mirrors.ustc.edu.cn/anaconda/>

## 说明

Anaconda 仓库镜像，**不包含商业使用需要授权的、由 Anaconda 公司维护的包（包括 Anaconda 安装器）**。目前镜像的部分有：

- Miniconda 安装包
- 由社区维护的 conda-forge 和 bioconda 频道的动态缓存

!!! warning "注意"

    从 2020 年起，在超过 200 人的组织中使用 **Anaconda 官方仓库**需要向 Anaconda 购买商业许可证。为保证已有兼容性，本镜像相关部分会全部重定向到 TUNA 镜像站。

    以下帮助**仅介绍如何配置 Miniconda 使用 conda-forge 和 bioconda 频道**。如果需要使用官方仓库，请使用其他镜像站，可参考 <https://help.mirrors.cernet.edu.cn/anaconda/> 中的帮助。

## 使用说明

### Miniconda

Miniconda（Anaconda 的轻量级替代）安装包可以在 <https://mirrors.ustc.edu.cn/anaconda/miniconda/> 下载。由于混用官方仓库与 conda-forge 可能导致问题，请运行以下命令找到已有的 `.condarc` 文件并删除 `defaults` 频道：

```console
$ conda config --show-sources
==> /root/miniconda3/.condarc <==
channels:
  - defaults
$ rm /root/miniconda3/.condarc
```

向用户的 `.condarc` 写入配置以使用镜像站，其中各个操作系统对应的文件：

- Linux & macOS: `$HOME/.condarc`
- Windows: `%USERPROFILE%\.condarc`
    - 由于 Windows 资源管理器的限制，可能需要先运行 `conda config --set show_channel_urls yes` 来生成这个文件。

内容如下：

```yaml
channels:
  - nodefaults
custom_channels:
  conda-forge: https://mirrors.ustc.edu.cn/anaconda/cloud
  bioconda: https://mirrors.ustc.edu.cn/anaconda/cloud
show_channel_urls: true
```

!!! info "Anaconda Cloud channels"

    目前我们为以下第三方频道提供**动态缓存**。与 [pypi](./pypi.md) 类似，未命中的包（包括未同步的频道）会重定向到 TUNA。

    - conda-forge
    - bioconda

之后运行 `conda clean -i` 清除缓存后，使用 `conda create -n myenv numpy -c conda-forge` 测试配置是否正确。

### Miniforge (Mamba)

Miniforge 是 conda-forge 官方维护的 Miniconda 替代品，默认使用 conda-forge 频道。安装包可以在 <https://mirrors.ustc.edu.cn/github-release/conda-forge/miniforge/LatestRelease/> 下载。

如果使用 Miniforge 提供的 `conda`，请参考上述 Miniconda 的配置方法。不过，Miniforge 通常会搭配 mamba 一起使用。mamba 是 conda 的一个高性能替代实现，用来解决 conda 速度慢的问题。

如果使用 `mamba`，其支持 `mirrored_channels` 选项，配置可以简化。`.condarc` 内容如下：

```yaml
channels:
  - conda-forge
mirrored_channels:
  conda-forge:
    - https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge
```

可以使用以下命令验证是否配置正确：

```sh
mamba config list --json | python -c "import sys, json; info = json.loads(sys.stdin.read()); print(info['mirrored_channels']['conda-forge'])"
```

## 相关链接

官方主页

:   <https://www.continuum.io/>
