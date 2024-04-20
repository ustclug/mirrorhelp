# Ubuntu Old Releases 源使用帮助

## 地址

<https://mirrors.ustc.edu.cn/ubuntu-old-releases/>

## 说明

Ubuntu 旧版本的软件源、镜像

## 收录架构

Ubuntu 曾经支持过的所有架构

## 收录版本

Ubuntu 曾经发布过的所有版本

## 使用说明

该仓库包含了所有 Ubuntu 以前发布过的软件仓库、镜像 ISO，但 Ubuntu
衍生版的 ISO 则不包含。

### 软件源

在 `/etc/apt/sources.list`{.interpreted-text role="file"}
文件中，将软件源的地址改为
`http://mirrors.ustc.edu.cn/ubuntu-old-releases/ubuntu`

更改完 `sources.list`{.interpreted-text role="file"} 文件后请运行
`sudo apt-get update` 更新索引以生效。

:::: tip
::: title
Tip
:::

使用 HTTPS 可以有效避免国内运营商的缓存劫持，但需要事先安装
`apt-transport-https`
::::

### 镜像

请前往 <https://mirrors.ustc.edu.cn/ubuntu-old-releases/releases/>
下载。

非 AMD64(x86_64), Intel x86 架构的镜像请前往
<https://mirrors.ustc.edu.cn/ubuntu-old-releases/releases/ports/releases/>
下载。
