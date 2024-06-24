# RPM Fusion

## 地址

<https://mirrors.ustc.edu.cn/rpmfusion/>

## 说明

RPM Fusion 是为 Fedora/RHEL 提供额外 RPM 软件包的第三方软件源。

## 使用说明

使用下列命令（在 bash 或兼容 shell 中），可以同时启用其 **free** 和 **nonfree** 软件源：

=== "Fedora 22 及更高版本"

    ```shell
    sudo dnf install https://mirrors.ustc.edu.cn/rpmfusion/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.ustc.edu.cn/rpmfusion/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
    ```

=== "RHEL 或兼容系统（如 Rocky Linux）"

    ```shell
    sudo dnf install https://mirrors.ustc.edu.cn/rpmfusion/free/el/rpmfusion-free-release-$(rpm -E %centos_ver).noarch.rpm https://mirrors.ustc.edu.cn/rpmfusion/nonfree/el/rpmfusion-nonfree-release-$(rpm -E %centos_ver).noarch.rpm
    ```

如果 `sudo` 不可用，你可以把以上命令中的 `sudo` 替换成 `su -c`。

## 替换源地址

!!! note

    RPM Fusion 默认使用 metalink 来根据用户发出请求的 IP 选择合适的镜像，通常情况下并不需要手动换源。

安装成功后，可使用下列命令备份并修改 `/etc/yum.repos.d/` 目录下以 `rpmfusion` 开头，以 `.repo` 结尾的文件。

- 具体而言，需要将文件中 `metalink=` 开头的行注释掉，取消 `baseurl=` 开头的行的注释并将等号后面链接中的 `http://download1.rpmfusion.org` 替换为 `https://mirrors.ustc.edu.cn/rpmfusion`：

    ```shell
    sudo sed -e 's|^metalink=|#metalink=|g' \
             -e 's|^#baseurl=http://download1.rpmfusion.org|baseurl=https://mirrors.ustc.edu.cn/rpmfusion|g' \
             -i.bak \
             /etc/yum.repos.d/rpmfusion*.repo
    ```

- 修改完成后，清除并重建缓存：

    ```shell
    sudo dnf clean all
    sudo dnf makecache
    ```

## 备注

在 RHEL 或兼容发行版（如 CentOS）上，您需要先启用 EPEL 源，请参考 [epel](epel.md)。

## 相关链接

项目主页

:   <https://rpmfusion.org>

邮件列表

:   <https://lists.rpmfusion.org>

用户配置指南（英文）

:   <https://rpmfusion.org/Configuration>
