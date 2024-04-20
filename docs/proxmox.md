# Proxmox 源使用帮助

## 地址

<https://mirrors.ustc.edu.cn/proxmox/>

## 说明

Proxmox 软件源

## 收录架构

所有 Proxmox 官方支持的架构

## 收录版本

所有 Proxmox 官方支持的版本

## 使用说明

:::: warning
::: title
Warning
:::

操作前请做好相应备份
::::

### Debian，Proxmox

一般情况下，需要同时修改基础系统（Debian）的源文件
`/etc/apt/sources.list`{.interpreted-text role="file"} 和 Proxmox
的源文件。

修改基础系统（Debian）的源文件，可以使用如下命令：

    sed -i 's|^deb http://ftp.debian.org|deb https://mirrors.ustc.edu.cn|g' /etc/apt/sources.list
    sed -i 's|^deb http://security.debian.org|deb https://mirrors.ustc.edu.cn/debian-security|g' /etc/apt/sources.list

修改 Proxmox 的源文件，可以使用如下命令：

    source /etc/os-release
    echo "deb https://mirrors.ustc.edu.cn/proxmox/debian/pve $VERSION_CODENAME pve-no-subscription" > /etc/apt/sources.list.d/pve-no-subscription.list

对于 Proxmox Backup Server 和 Proxmox Mail Gateway，请将以上命令中的
`pve` 分别替换为 `pbs` 和 `pmg`。

PVE 8 之后默认安装 ceph 仓库源文件
`/etc/apt/sources.list.d/ceph.list`，可以使用如下命令更换源：

    if [ -f /etc/apt/sources.list.d/ceph.list ]; then CEPH_CODENAME=`ceph -v | grep ceph | awk '{print $(NF-1)}'`; source /etc/os-release; echo "deb https://mirrors.ustc.edu.cn/proxmox/debian/ceph-$CEPH_CODENAME $VERSION_CODENAME no-subscription" > /etc/apt/sources.list.d/ceph.list; fi

更改完 `sources.list`{.interpreted-text role="file"} 文件后请运行
`apt update` 更新索引以生效。

### CT Templates

另外，如果你需要使用 Proxmox 网页端下载 CT Templates，可以替换 CT
Templates 的源为 `http://mirrors.ustc.edu.cn`。

具体方法：将 `/usr/share/perl5/PVE/APLInfo.pm`{.interpreted-text
role="file"} 文件中默认的源地址 `http://download.proxmox.com` 替换为
`https://mirrors.ustc.edu.cn/proxmox` 即可。

可以使用如下命令：

    cp /usr/share/perl5/PVE/APLInfo.pm /usr/share/perl5/PVE/APLInfo.pm_back
    sed -i 's|http://download.proxmox.com|https://mirrors.ustc.edu.cn/proxmox|g' /usr/share/perl5/PVE/APLInfo.pm 

针对 `/usr/share/perl5/PVE/APLInfo.pm`{.interpreted-text role="file"}
文件的修改，执行\`systemctl restart pvedaemon\`后生效。
