# RPM Fusion

## 地址

<https://mirrors.ustc.edu.cn/rpmfusion/>

## 说明

RPM Fusion 是为 Fedora/RHEL 提供额外 RPM 软件包的第三方软件源。

## 使用说明

使用下列命令（在 bash 或兼容 shell 中），可以同时启用其 **free** 和
**nonfree** 软件源：

-   Fedora 22 及更高版本:

        sudo dnf install https://mirrors.ustc.edu.cn/rpmfusion/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.ustc.edu.cn/rpmfusion/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm

-   RHEL 6 或兼容系统（如 CentOS ）:

        sudo yum localinstall --nogpgcheck https://mirrors.ustc.edu.cn/rpmfusion/free/el/rpmfusion-free-release-6.noarch.rpm https://mirrors.ustc.edu.cn/rpmfusion/nonfree/el/rpmfusion-nonfree-release-6.noarch.rpm

-   RHEL ７ 或兼容系统（如 CentOS ）:

        sudo yum localinstall --nogpgcheck https://mirrors.ustc.edu.cn/rpmfusion/free/el/rpmfusion-free-release-7.noarch.rpm https://mirrors.ustc.edu.cn/rpmfusion/nonfree/el/rpmfusion-nonfree-release-7.noarch.rpm

如果 `sudo` 不可用，你可以把以上命令中的 `sudo` 替换成 `su -c` 。

## 备注

在 RHEL 或兼容发行版（如 CentOS ）上，您需要先启用 EPEL 源，请参考
`epel`{.interpreted-text role="doc"}。

## 相关链接

项目主页

:   <https://rpmfusion.org>

邮件列表

:   <https://lists.rpmfusion.org>

用户配置指南（英文）

:   <https://rpmfusion.org/Configuration>
