# Packaging Gitea 打包

## 地址

<https://mirrors.ustc.edu.cn/packaging-gitea/>

## 说明

这是对 <https://gitlab.com/packaging/gitea> 的内容镜像，用于为 Debian/Ubuntu 用户提供基于 `apt` 的 Gitea 包管理安装方式。需要注意的是，该仓库由社区维护，并由 Gitea 官方文档于 <https://docs.gitea.com/installation/install-from-package#others> 列出，不由 Gitea 官方直接提供。

## 收录架构

- aarch64
- x86_64

## 使用说明

添加仓库签名密钥：

```shell
sudo curl -sL -o /etc/apt/trusted.gpg.d/morph027-gitea.asc https://packaging.gitlab.io/gitea/gpg.key
```

添加镜像源：

```shell
echo "deb https://mirrors.ustc.edu.cn/packaging-gitea gitea main" | sudo tee /etc/apt/sources.list.d/morph027-gitea.list
```

安装：

```shell
sudo apt-get update
sudo apt-get install gitea morph027-keyring
```

启动：

```shell
systemctl enable gitea --now
```

查看服务状态：

```shell
systemctl status gitea
```
