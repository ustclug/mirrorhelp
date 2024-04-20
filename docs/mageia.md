# Mageia

!!! warning

    Mageia 源于 2018 年 11 月起转为反向代理服务（详见 [mageia
    镜像变更通知](https://servers.ustclug.org/2018/11/mageia-mirror-change/)），并于
    2022 年 1 月改为重定向至其他教育网镜像站。

## 地址

<https://mirrors.ustc.edu.cn/mageia/>

## 说明

Mageia Linux 软件源。

## 收录架构

x86_64，i686

## 收录版本

所有仍在支持的版本，最新测试版本和 Cauldron 滚动更新开发版

## 使用说明

从 Mageia 6 开始，Mageia 的软件仓库同时兼容 urpmi 和
dnf，两个包管理器默认情况下均被预装。由于在可预见的未来里，urpmi
仍是默认包管理器且 Mageia 控制中心也只调用 urpmi，所以 urpmi
是必须要配置好的，而 dnf 可以按你的实际需要选择是否进行配置。

### urpmi 配置方法

移除所有已添加的软件仓库（sudo
似乎是没有被预装的，可以在稍后再安装使用）：

    su
    urpmi.removemedia -a

添加中科大的软件源，以 Mageia 6，x86_64 架构为例：

    su
    urpmi.addmedia --distrib https://mirrors.ustc.edu.cn/mageia/distrib/6/x86_64

刷新缓存：

    su
    urpmi.update -a

### dnf 配置方法

dnf 在默认情况下已经被预装，如果你发现并没有，可以使用 urpmi 安装：

    su
    urpmi mageia-repos dnf

接下来编辑 `/etc/yum.repos.d/` 中的文件：

将所有文件中的：

    #baseurl=https://mirrors.kernel.org/mageia/

替换为：

    baseurl=https://mirrors.ustc.edu.cn/mageia/

!!! tip

    为了让 dnf
    能在中科大软件源出现问题时，自动切换至其它后备软件源，我们不建议你注释掉
    mirrorlist 行。

为了避免 dnf 和 urpmi
启用的软件仓库不一致，在保存之前，还需要额外进行检查，查看 urpmi
已启用仓库的方法如下：

-   打开 Mageia 控制中心。
-   选择配置安装和更新所用的介质源。

默认情况下，一个使用 x86_64 架构的 Mageia 在 urpmi 下默认启用的仓库有：

-   Core Release
-   Core Updates
-   Nonfree Release
-   Nonfree Updates
-   Core 32bit Release
-   Core 32bit Updates
-   Nonfree 32bit Release
-   Nonfree 32bit Updates

接下来，逐个检查文件，确认 urpmi 已仓库在 dnf 也被已启用，依然是编辑
`/etc/yum.repos.d/` 中的文件：

以 `/etc/yum.repos.d/mageia-x86_64.repo`
为例：

```ini
[mageia-x86_64]
name=Mageia $releasever - x86_64
baseurl=https://mirrors.ustc.edu.cn/mageia/distrib/$releasever/x86_64/media/core/release/
#metalink=https://mirrors.mageia.org/metalink?distrib=mageia-$releasever&arch=x86_64&section=core&repo=release
mirrorlist=https://www.mageia.org/mirrorlist/?release=$releasever&arch=x86_64&section=core&repo=release
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-Mageia
failovermethod=priority
enabled=1

[updates-x86_64]
name=Mageia $releasever - x86_64 - Updates
baseurl=https://mirrors.ustc.edu.cn/mageia/distrib/$releasever/x86_64/media/core/updates/
#metalink=https://mirrors.mageia.org/metalink?distrib=mageia-$releasever&arch=x86_64&section=core&repo=updates
mirrorlist=https://www.mageia.org/mirrorlist/?release=$releasever&arch=x86_64&section=core&repo=updates
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-Mageia
failovermethod=priority
enabled=1

[updates_testing-x86_64]
name=Mageia $releasever - x86_64 - Test Updates
baseurl=https://mirrors.ustc.edu.cn/mageia/distrib/$releasever/x86_64/media/core/updates_testing/
#metalink=https://mirrors.mageia.org/metalink?distrib=mageia-$releasever&arch=x86_64&section=core&repo=updates_testing
mirrorlist=https://www.mageia.org/mirrorlist/?release=$releasever&arch=x86_64&section=core&repo=updates_testing
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-Mageia
failovermethod=priority
enabled=0

[backports-x86_64]
name=Mageia $releasever - x86_64 - Backports
baseurl=https://mirrors.ustc.edu.cn/mageia/distrib/$releasever/x86_64/media/core/backports/
#metalink=https://mirrors.mageia.org/metalink?distrib=mageia-$releasever&arch=x86_64&section=core&repo=backports
mirrorlist=https://www.mageia.org/mirrorlist/?release=$releasever&arch=x86_64&section=core&repo=backports
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-Mageia
failovermethod=priority
enabled=0

[backports_testing-x86_64]
name=Mageia $releasever - x86_64 - Test Backports
baseurl=https://mirrors.ustc.edu.cn/mageia/distrib/$releasever/x86_64/media/core/backports_testing/
#metalink=https://mirrors.mageia.org/metalink?distrib=mageia-$releasever&arch=x86_64&section=core&repo=backports_testing
mirrorlist=https://www.mageia.org/mirrorlist/?release=$releasever&arch=x86_64&section=core&repo=backports_testing
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-Mageia
failovermethod=priority
enabled=0

[mageia-x86_64-debuginfo]
name=Mageia $releasever - x86_64 - Debug
baseurl=https://mirrors.ustc.edu.cn/mageia/distrib/$releasever/x86_64/media/debug/core/release/
#metalink=https://mirrors.mageia.org/metalink?distrib=mageia-$releasever&arch=x86_64&section=core&repo=release&debug=true
mirrorlist=https://www.mageia.org/mirrorlist/?release=$releasever&arch=x86_64&section=core&repo=release&debug=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-Mageia
failovermethod=priority
enabled=0

[updates-x86_64-debuginfo]
name=Mageia $releasever - x86_64 - Updates - Debug
baseurl=https://mirrors.ustc.edu.cn/mageia/distrib/$releasever/x86_64/media/debug/core/updates/
#metalink=https://mirrors.mageia.org/metalink?distrib=mageia-$releasever&arch=x86_64&section=core&repo=updates&debug=true
mirrorlist=https://www.mageia.org/mirrorlist/?release=$releasever&arch=x86_64&section=core&repo=updates&debug=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-Mageia
failovermethod=priority
enabled=0

[updates_testing-x86_64-debuginfo]
name=Mageia $releasever - x86_64 - Test Updates - Debug
baseurl=https://mirrors.ustc.edu.cn/mageia/distrib/$releasever/x86_64/media/debug/core/updates_testing/
#metalink=https://mirrors.mageia.org/metalink?distrib=mageia-$releasever&arch=x86_64&section=core&repo=updates_testing&debug=true
mirrorlist=https://www.mageia.org/mirrorlist/?release=$releasever&arch=x86_64&section=core&repo=updates_testing&debug=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-Mageia
failovermethod=priority
enabled=0

[backports-x86_64-debuginfo]
name=Mageia $releasever - x86_64 - Backports - Debug
baseurl=https://mirrors.ustc.edu.cn/mageia/distrib/$releasever/x86_64/media/debug/core/backports/
#metalink=https://mirrors.mageia.org/metalink?distrib=mageia-$releasever&arch=x86_64&section=core&repo=backports&debug=true
mirrorlist=https://www.mageia.org/mirrorlist/?release=$releasever&arch=x86_64&section=core&repo=backports&debug=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-Mageia
failovermethod=priority
enabled=0

[backports_testing-x86_64-debuginfo]
name=Mageia $releasever - x86_64 - Test Backports - Debug
baseurl=https://mirrors.ustc.edu.cn/mageia/distrib/$releasever/x86_64/media/debug/core/backports_testing/
#metalink=https://mirrors.mageia.org/metalink?distrib=mageia-$releasever&arch=x86_64&section=core&repo=backports_testing&debug=true
mirrorlist=https://www.mageia.org/mirrorlist/?release=$releasever&arch=x86_64&section=core&repo=backports_testing&debug=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-Mageia
failovermethod=priority
enabled=0
```

你需要确认所有需要开启的软件仓库，如上面这个文件中的 \[mageia-x86_64\]
和 \[updates-x86_64\] （即 Core Release 和 Core Updates）部分末端
enabled 值为 1，即：

    enabled=1

其它所有不启用的仓库 enabled 值为 0，即：

    enabled=0

保存所有的文件，退出。

刷新缓存：

    su
    dnf makecache 

## 相关链接

官方主页

:   <https://www.mageia.org/>

邮件列表

:   <https://www.mageia.org/mailman/>

论坛

:   <https://forums.mageia.org/>

文档

:   <https://www.mageia.org/en/doc/>

Wiki

:   <https://wiki.mageia.org/>

镜像列表

:   <https://mirrors.mageia.org/>
