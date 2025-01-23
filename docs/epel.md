# EPEL

## 地址

<https://mirrors.ustc.edu.cn/epel/>

## 说明

EPEL (Extra Packages for Enterprise Linux) 是由 Fedora Special Interest Group 为企业 Linux 创建、维护和管理的一个高质量附加包集合，适用于但不仅限于 Red Hat Enterprise Linux (RHEL) 及其衍生发行版。

## 收录架构

官方支持的所有架构

## 收录版本

官方支持的所有版本

## 使用说明

!!! note

    本镜像不包含 EPEL Cisco OpenH264 仓库。

!!! warning

    操作前请做好相应备份。

执行以下命令：

```shell
sudo dnf install -y epel-release
sudo sed -e 's|^metalink=|#metalink=|g' \
         -e 's|^#baseurl=https\?://download.fedoraproject.org/pub/epel/|baseurl=https://mirrors.ustc.edu.cn/epel/|g' \
         -e 's|^#baseurl=https\?://download.example/pub/epel/|baseurl=https://mirrors.ustc.edu.cn/epel/|g' \
         -i.bak \
         /etc/yum.repos.d/epel{,-testing}.repo
```

以下是替换之后的 `/etc/yum.repos.d/epel.repo`
 文件：

```ini title="/etc/yum.repos.d/epel.repo"
[epel]
name=Extra Packages for Enterprise Linux $releasever - $basearch
# It is much more secure to use the metalink, but if you wish to use a local mirror
# place its address here.
baseurl=https://mirrors.ustc.edu.cn/epel/$releasever/Everything/$basearch/
#metalink=https://mirrors.fedoraproject.org/metalink?repo=epel-$releasever&arch=$basearch&infra=$infra&content=$contentdir
enabled=1
gpgcheck=1
countme=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-$releasever

[epel-debuginfo]
name=Extra Packages for Enterprise Linux $releasever - $basearch - Debug
# It is much more secure to use the metalink, but if you wish to use a local mirror
# place its address here.
baseurl=https://mirrors.ustc.edu.cn/epel/$releasever/Everything/$basearch/debug/
#metalink=https://mirrors.fedoraproject.org/metalink?repo=epel-debug-$releasever&arch=$basearch&infra=$infra&content=$contentdir
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-$releasever
gpgcheck=1

[epel-source]
name=Extra Packages for Enterprise Linux $releasever - $basearch - Source
# It is much more secure to use the metalink, but if you wish to use a local mirror
# place its address here.
baseurl=https://mirrors.ustc.edu.cn/epel/$releasever/Everything/source/tree/
#metalink=https://mirrors.fedoraproject.org/metalink?repo=epel-source-$releasever&arch=$basearch&infra=$infra&content=$contentdir
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-$releasever
gpgcheck=1
```

## 相关链接

Wiki

:   <https://fedoraproject.org/wiki/EPEL>

FAQ

:   <https://fedoraproject.org/wiki/EPEL/FAQ>
