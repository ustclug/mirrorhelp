# AOSP

## 地址

<https://mirrors.ustc.edu.cn/aosp/>

## 说明

Android 开源项目源代码镜像。支持 git 与 http(s) 协议。关于协议选择，请参考[此处的说明](#http_sync)。

## 初始同步

### 初始同步方法 1（推荐）

第一次同步数据量特别大，如果网络不稳定，中间失败就要从头再来了。所以我们提供了打包的
AOSP 镜像，为一个 tar 包，截至 2024 年 3 月约 80G（注意磁盘格式需要能够支持大文件）。
这样就可以通过 HTTP(S) 的方式下载，支持断点续传。

下载地址：<https://mirrors.ustc.edu.cn/aosp-monthly/>。
**请注意对比 checksum。**

然后解压后根据[下文的方法](#change_to_ustc)更改同步地址，
然后用命令 `repo sync` 就可以把代码都 checkout 出来。

该 tar 包为定时从 <https://mirrors.tuna.tsinghua.edu.cn/aosp-monthly/> 下载。

### 初始同步方法 2（不推荐）

!!! warning

    由于 AOSP 镜像造成的 IO 负载很高，请**不要**使用以下方式初次同步。

按照 [Google 官方教程](https://source.android.com/source/downloading.html)
([CN](https://source.android.google.cn/source/downloading))，
将 `https://android.googlesource.com/platform/manifest` 替换为
`git://mirrors.ustc.edu.cn/aosp/platform/manifest` 或
`http://mirrors.ustc.edu.cn/aosp/platform/manifest`。

具体做法摘录如下：首先下载 repo 工具。

```shell
mkdir ~/bin
PATH=~/bin:$PATH
curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
## 如果上述 URL 不可访问，可以用下面的：
## curl -sSL 'https://gerrit-googlesource.proxy.ustclug.org/git-repo/+/main/repo?format=TEXT' | base64 -d > ~/bin/repo
chmod a+x ~/bin/repo
```

然后建立一个工作目录（名字任意）：

```shell
mkdir WORKING_DIRECTORY
cd WORKING_DIRECTORY
```

初始化仓库：

```shell
# 如果提示无法连接到 gerrit.googlesource.com，可以设置 REPO_URL 环境变量：
export REPO_URL=https://gerrit-googlesource.proxy.ustclug.org/git-repo
repo init -u git://mirrors.ustc.edu.cn/aosp/platform/manifest
```

如果需要某个特定的 Android 版本
（[Android 版本列表](https://source.android.com/source/build-numbers.html#source-code-tags-and-builds)
([CN](https://source.android.google.cn/source/build-numbers?hl=zh-cn#source-code-tags-and-builds))，
[镜像站 tags 列表](http://mirrors.ustc.edu.cn/aosp/platform/manifest.git/refs/tags/)）：

```shell
repo init -u git://mirrors.ustc.edu.cn/aosp/platform/manifest -b android-4.0.1_r1
```

同步源码树（以后只需执行这条命令来同步）：

```shell
repo sync
```

## 已有仓库如何改用科大源 {#change_to_ustc}

如果您已经从官方同步了 AOSP 仓库，现在希望使用科大的 AOSP 仓库，请修改
`.repo/manifests.git/config`，将：

```shell
url = https://android.googlesource.com/platform/manifest
```

修改成：

```shell
url = git://mirrors.ustc.edu.cn/aosp/platform/manifest
```

即可。

## 通过 HTTP(S) 协议同步 {#http_sync}

以上说明中，默认使用了 git 协议的地址：`git://mirrors.ustc.edu.cn/aosp/platform/manifest`。

如果由于某种原因不能通过 git 协议同步，请修改 `.repo/manifests.git/config`，将

```shell
url = git://mirrors.ustc.edu.cn/aosp/platform/manifest
```

修改成 (HTTP)：

```shell
url = http://mirrors.ustc.edu.cn/aosp/platform/manifest
```

或 (HTTPS)：

```shell
url = https://mirrors.ustc.edu.cn/aosp/platform/manifest
```

通过 HTTP(S) 同步过程中可能提示 clone.bundle 404 错误，这是正常现象，可以忽略。

## 使用时间段与并发设置建议

1. 本镜像每天凌晨 04:30
    同步一次。同步可能需要较长时间，因此使用本镜像时建议避开凌晨 04:30
    ～ 06:00 这段时间。
2. 由于硬盘 I/O 资源有限，Git 服务器每 IP 限制 5 个并发连接。
    `repo sync` 命令默认使用 4 个并发连接，请勿使用 `-j`
    参数增加并发连接数。

## 附录：Brillo

Brillo 项目的代码托管在 AOSP 项目中，Mirrors 镜像的是整个 AOSP
项目，所以自然也能从本镜像下载 Brillo 项目代码。

参考 Brillo 官方文档
<https://developers.google.com/brillo/docs/reference/downloads>
进行下载，将其中源码 manifest 地址改为
`git://mirrors.ustc.edu.cn/aosp/brillo/manifest`。即：

`repo init` 时，使用
`repo init -u git://mirrors.ustc.edu.cn/aosp/brillo/manifest -b master`

## 相关链接

Android 开源项目官网

:   <https://source.android.com/>

Android 开源项目官网 (CN)

:   <https://source.android.google.cn/>

Android Code Search

:   <https://cs.android.com/>
