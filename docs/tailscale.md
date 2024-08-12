# Tailscale

<https://mirrors.ustc.edu.cn/tailscale/>

## 收录版本

- 软件版本：Stable
- 发行版：受支持的 Debian 版本与 Ubuntu LTS 版本
- 架构：除 MIPS 以外的所有架构

## 使用说明

参考 [Tailscale 的安装教程](https://tailscale.com/kb/1031/install-linux)，在安装完成后替换软件源：

```shell
sudo sed -i 's,pkgs.tailscale.com/stable,mirrors.ustc.edu.cn/tailscale,g' /etc/apt/sources.list.d/tailscale.list
```

然后执行 `sudo apt update` 刷新软件包缓存。
