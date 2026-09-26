# Fedora

## 地址

<https://mirrors.ustc.edu.cn/fedora/>

## 说明

Fedora 软件源

## 收录架构

x86_64

## 收录版本

所有仍在支持的版本

## 使用说明

!!! note

    Fedora 默认使用 metalink 来根据用户发出请求的 IP 选择合适的镜像，通常情况下并不需要手动换源。

!!! warning

    操作前请做好相应备份。

=== "Fedora >= 44"

    建议通过 DNF5 覆写仓库配置：

    ```shell
    sudo dnf config-manager setopt \
        fedora.baseurl='https://mirrors.ustc.edu.cn/fedora/releases/$releasever/Everything/$basearch/os/' \
        fedora.metalink= \
        updates.baseurl='https://mirrors.ustc.edu.cn/fedora/updates/$releasever/Everything/$basearch/' \
        updates.metalink=
    ```

    该命令会在 `/etc/dnf/repos.override.d/99-config_manager.repo` 中写入覆写配置。

    或者先创建覆写目录：

    ```shell
    sudo mkdir -p /etc/dnf/repos.override.d
    ```

    然后将以下内容保存为 `/etc/dnf/repos.override.d/99-ustc.repo`：

    ```ini title="/etc/dnf/repos.override.d/99-ustc.repo"
    --8<-- "fedora-override.repo"
    ```

    !!! note

        Fedora 45 的[仓库配置迁移](https://fedoraproject.org/wiki/Changes/RelocateRpmRepoConfigsToUsr)将系统提供的 `.repo` 文件从 `/etc/yum.repos.d` 移至 `/usr/share/dnf5/repos.d`。
        上述覆写方式适用于这两种布局，并保留系统提供的 GPG 密钥路径等配置。

=== "Fedora 39–43"

    用以下命令替换 `/etc/yum.repos.d` 下的文件：

    ```shell
    sudo sed -e 's|^metalink=|#metalink=|g' \
             -e 's|^#baseurl=http://download.example/pub/fedora/linux|baseurl=https://mirrors.ustc.edu.cn/fedora|g' \
             -i.bak \
             /etc/yum.repos.d/fedora.repo \
             /etc/yum.repos.d/fedora-updates.repo
    ```

    或者直接复制以下文件：

    ```ini title="/etc/yum.repos.d/fedora.repo"
    --8<-- "fedora.repo"
    ```

    ```ini title="/etc/yum.repos.d/fedora-updates.repo"
    --8<-- "fedora-updates.repo"
    ```

最后运行 `sudo dnf makecache` 生成缓存。

## 相关链接

官方主页

:   <https://getfedora.org/>

邮件列表

:   <https://fedoraproject.org/wiki/Communicating_and_getting_help>

论坛

:   <https://forums.fedoraforum.org/>

文档

:   <https://docs.fedoraproject.org/>

Wiki

:   <https://fedoraproject.org/wiki/>

镜像列表

:   <https://admin.fedoraproject.org/mirrormanager>
