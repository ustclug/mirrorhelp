# Tailscale

## 地址

<https://mirrors.ustc.edu.cn/tailscale/>

## 说明

Tailscale 镜像

## 收录版本

Stable 版本的 Debian 与 Ubuntu 系统的安装包，除 MIPS 以外的所有架构

## 使用说明

参考 [Tailscale 的安装教程](https://tailscale.com/kb/1031/install-linux)，在安装完成后替换软件源：

```shell
sudo sed -i 's,pkgs.tailscale.com/stable,mirrors.ustc.edu.cn/tailscale,g' /etc/apt/sources.list.d/tailscale.list
```

然后执行 `sudo apt update` 刷新软件包缓存。
