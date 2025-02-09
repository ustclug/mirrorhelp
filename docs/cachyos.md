# CachyOS

## 地址

<https://mirrors.ustc.edu.cn/cachyos/>

## 说明

CachyOS 软件源

## 收录架构

x86_64

## 使用说明

编辑 `/etc/pacman.d/cachyos-mirrorlist`，在文件的最顶端添加

```ini
Server = https://mirrors.ustc.edu.cn/cachyos/repo/$arch/$repo
```

编辑 `/etc/pacman.d/cachyos-v3-mirrorlist`，在文件的最顶端添加

```ini
Server = https://mirrors.ustc.edu.cn/cachyos/repo/$arch_v3/$repo
```

编辑 `/etc/pacman.d/cachyos-v4-mirrorlist`，在文件的最顶端添加

```ini
Server = https://mirrors.ustc.edu.cn/cachyos/repo/$arch_v4/$repo
```

## 相关链接

官方主页

:   <https://cachyos.org/>

论坛

:   <https://discuss.cachyos.org/>

Wiki

:   <https://wiki.cachyos.org/>
