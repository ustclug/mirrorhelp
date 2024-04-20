# Kali Linux

## 地址

<https://mirrors.ustc.edu.cn/kali/>

## 说明

Kali Linux 软件源

## 支持的系统架构

amd64, armel, armhf, i386

## 使用说明

编辑 `/etc/apt/sources.list`{.interpreted-text role="file"} 文件,
在文件最前面添加以下条目：

    deb https://mirrors.ustc.edu.cn/kali kali-rolling main non-free non-free-firmware contrib
    deb-src https://mirrors.ustc.edu.cn/kali kali-rolling main non-free non-free-firmware contrib

更改完 `sources.list`{.interpreted-text role="file"} 文件后请运行
`sudo apt-get update` 更新索引以生效。

!!! warning

    由于 Kali 仓库未使用 by-hash
    机制，同步时的一致性无法保证。如果在同步时执行
    `apt update`，可能会看到以下错误

        E: 无法下载 https://mirrors.ustc.edu.cn/kali/dists/kali-rolling/main/source/Sources.gz 文件尺寸不符(14593053 != 14592993)。您使用的镜像正在同步中？

    如果出现以上错误，则需等待同步完成后再执行 `apt update`。

## 相关链接

Kali Linux 主页

:   <https://www.kali.org/>

论坛

:   <http://forums.kali.org/>

文档

:   <https://www.kali.org/kali-linux-documentation/>
