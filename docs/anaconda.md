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

## 相关链接

官方主页

:   <https://www.continuum.io/>

## Pixi

Pixi 是一个高效、跨平台的包管理与环境管理工具，构建于 Conda 生态之上，专为科研与数据科学工作流设计。[Github地址](https://github.com/prefix-dev/pixi)


Pixi 也支持镜像配置，你可以参考 [此文档](https://pixi.sh/latest/reference/pixi_configuration/#mirrors) 将「科大镜像」源添加到你的配置文件里。

配置 `config.toml` 如下:

```shell
[mirrors]
"https://conda.anaconda.org/conda-forge" = ["https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge"]
"https://conda.anaconda.org/main" = ["https://mirrors.ustc.edu.cn/anaconda/pkgs/main"]
"https://prefix.dev/conda-forge" = ["https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge"]
```

如果是项目级别的镜像配置，请配置在此目录：`your_project/.pixi/config.toml`；如果是全局配置，请配置在此目录：`$HOME/.pixi/config.toml`。更多自定义级别的配置，请参考[配置文档](https://pixi.sh/latest/reference/pixi_configuration/)

如需验证镜像是否生效，可尝试使用`sudo tcpdump -i any port 443 | grep ustc` 来监听第三方包的下载:

```shell
# 在一个终端运行
sudo tcpdump -i any host mirrors.ustc.edu.cn

# 在另一个终端安装包
pixi add numpy
```
如果看到数据包输出`IP mirrors.ustc.edu.cn.https`，说明正在从 「科大镜像站」下载。

注意：`pixi.lock` 文件中记录的可能仍是原始的 conda.anaconda.org 地址，但实际下载时 pixi 会根据镜像配置自动重定向到 「科大镜像」，这是正常现象。