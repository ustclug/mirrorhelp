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

Pixi 是一个高效跨平台的包管理器和环境管理工具，专为科研与数据科学工作流设计。[Github地址](https://github.com/prefix-dev/pixi)

它由 Mamba 背后的团队打造，构建于 `Conda` 和 `conda-forge` 生态之上，深度集成 `uv`，致力于提供：

* 可复现性：通过锁文件 `pixi.lock`，确保在任何设备上都能还原完全一致的运行环境；
* 协作友好：一条命令自动安装依赖、执行任务，让团队协作更轻松；
* 硬件兼容：原生支持 CUDA 等硬件加速，无需容器化；
* 多语言支持：不仅支持 Python 包，还支持 C/C++、Rust 等多种生态；
* 教学利器：帮助教师为不同系统的学生统一环境，只需一条命令即可部署。

除了 Anaconda 以外，Pixi 的 channel 还支持 conda-forge、nvidia、pytorch 等，也支持自定义 channel。

Pixi 也支持镜像配置，你可以参考 [此文档](https://pixi.sh/latest/reference/pixi_configuration/#mirrors) 将`tuna` 镜像源添加到你的配置文件里。

![Pixi logo](https://raw.githubusercontent.com/prefix-dev/pixi/refs/heads/main/docs/assets/pixi.webp)
