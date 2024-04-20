# Manjaro Linux 源使用帮助

## 地址

<https://mirrors.ustc.edu.cn/manjaro/>

## 说明

Manjaro Linux 软件源

## 收录版本

Stable, Testing, Unstable

## 收录架构

i686, x86_64, AArch64

:::: tip
::: title
Tip
:::

目前 AArch64 (ARM) 架构的 manjaro 源位于主源，manjaro-arm
镜像上游已不再更新。
::::

## 使用说明

生成可用中国镜像站列表：

    sudo pacman-mirrors -i -c China -m rank

勾选 `http://mirrors.ustc.edu.cn/manjaro/` ，然后按 `OK` 键两次。

最后刷新缓存：

    sudo pacman -Syy

## 相关链接

官方主页

:   <https://www.manjaro.org/>

邮件列表

:   <https://lists.manjaro.org/mailman/listinfo>

论坛

:   <https://forum.manjaro.org/>

Wiki

:   <https://wiki.manjaro.org/>
