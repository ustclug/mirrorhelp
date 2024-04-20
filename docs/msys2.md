# MSYS2 源使用帮助

## 地址

<https://mirrors.ustc.edu.cn/msys2/>

## 说明

MSYS2 镜像

## 收录架构

-   MINGW: i686, x86_64
-   MSYS: i686, x86_64

## 获取基本组件包

访问该镜像目录下的 `distrib/`
目录（[x86_64](http://mirrors.ustc.edu.cn/msys2/distrib/x86_64/)、[i686](http://mirrors.ustc.edu.cn/msys2/distrib/i686/)），找到名为
`msys2-<架构>-<日期>.exe` 的文件 （如
`msys2-x86_64-20141113.exe`），下载安装即可。

## Pacman 的配置

在 MSYS2 环境下直接运行命令替换镜像源：

    sed -i "s#mirror.msys2.org/#mirrors.ustc.edu.cn/msys2/#g" /etc/pacman.d/mirrorlist*

然后执行 `pacman -Sy` 刷新软件包数据即可。

## 相关链接

MSYS2 主页

:   <https://www.msys2.org/>
