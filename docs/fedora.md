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

    Fedora 默认使用 metalink 来根据用户发出请求的 IP 选择合适的镜像。通常情况下以下配置并不需要。

!!! warning

    操作前请做好相应备份。

=== "Fedora >= 39"

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

    !!! note

        Fedora 39 起 modular 仓库已经不复存在（详见 <https://fedoraproject.org/wiki/Changes/RetireModularity>）。
        因此 Fedora 39 及以上的版本不需要修改 `fedora-modular.repo` 和 `fedora-updates-modular.repo`。

=== "Fedora <= 38"

    用以下命令替换 `/etc/yum.repos.d` 下的文件：

    ```shell
    sudo sed -e 's|^metalink=|#metalink=|g' \
             -e 's|^#baseurl=http://download.example/pub/fedora/linux|baseurl=https://mirrors.ustc.edu.cn/fedora|g' \
             -i.bak \
             /etc/yum.repos.d/fedora.repo \
             /etc/yum.repos.d/fedora-modular.repo \
             /etc/yum.repos.d/fedora-updates.repo \
             /etc/yum.repos.d/fedora-updates-modular.repo
    ```

    或者直接复制以下文件：

    ```ini title="/etc/yum.repos.d/fedora.repo"
    --8<-- "fedora.repo"
    ```

    ```ini title="/etc/yum.repos.d/fedora-updates.repo"
    --8<-- "fedora-updates.repo"
    ```

    ```ini title="/etc/yum.repos.d/fedora-modular.repo"
    --8<-- "fedora-modular.repo"
    ```

    ```ini title="/etc/yum.repos.d/fedora-updates-modular.repo"
    --8<-- "fedora-updates-modular.repo"
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
