# CentOS Vault

!!! warning "警告"

    CentOS 7 已于 2024 年 6 月 30 日结束维护，我们强烈建议立即迁移到其他解决方案。

    我们不对 CentOS Vault 镜像的稳定性及可用性作出任何保证。

## 地址

<https://mirrors.ustc.edu.cn/centos-vault/>

## 说明

CentOS 归档软件源

## 收录版本

所有**已停止维护**的版本

## 使用说明

!!! warning

    操作前请做好相应备份。

对于 CentOS 7，使用以下命令替换默认配置

```shell
sudo sed -i.bak \
  -e 's|^mirrorlist=|#mirrorlist=|g' \
  -e 's|^#baseurl=http://mirror.centos.org/centos|baseurl=https://mirrors.ustc.edu.cn/centos-vault/centos|g' \
  /etc/yum.repos.d/CentOS-Base.repo
```

以上命令只替换了默认启用的仓库。替换之后请运行 `yum makecache` 更新缓存。

以下是替换之后的文件：

=== "CentOS 7"

    ```ini title="/etc/yum.repos.d/CentOS-Base.repo"
    --8<-- "centos7/CentOS-Base.repo"
    ```
