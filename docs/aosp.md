# AOSP

## 地址

<https://mirrors.ustc.edu.cn/aosp/>

## 说明与 `repo` 工具安装

Android 开源项目源代码镜像。支持 https 协议。git 协议在未来可能会被移除。

AOSP 代码使用 `repo` 工具管理，因此进行下面的步骤前**必须**先安装 `repo` 工具：

```shell
mkdir ~/bin
PATH=~/bin:$PATH
curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
## 如果上述 URL 不可访问，可以用下面的：
## curl -sSL 'https://gerrit-googlesource.proxy.ustclug.org/git-repo/+/main/repo?format=TEXT' | base64 -d > ~/bin/repo
chmod a+x ~/bin/repo
```

以下介绍假设你已经在 `~/bin` 目录下安装了 `repo` 工具，并且将 `~/bin` 添加到了 `$PATH` 环境变量中。

## 初始同步

第一次同步数据量特别大，如果网络不稳定，中间失败就要从头再来了。所以我们提供了打包的 AOSP 镜像，为一个 tar 包，截至 2024 年 3 月约 80G（注意磁盘格式需要能够支持大文件）。这样就可以通过 HTTP(S) 的方式下载，支持断点续传。该 tar 包为定时从 [TUNA](https://mirrors.tuna.tsinghua.edu.cn/aosp-monthly/) 下载。

下载地址：<https://mirrors.ustc.edu.cn/aosp-monthly/>。**请注意对比 checksum。**

解压、修改配置并同步：

```shell
tar xf aosp-latest.tar
cd AOSP
git -C ./.repo/manifests.git/ remote set-url origin https://mirrors.ustc.edu.cn/aosp/platform/manifest.git
repo sync
```

## 初始同步特定分支

以下内容参考 [Google 官方教程](https://source.android.com/source/downloading.html)([CN](https://source.android.google.cn/source/downloading))。

建立一个工作目录（名字任意）：

```shell
mkdir WORKING_DIRECTORY
cd WORKING_DIRECTORY
```

根据你所需要的 Android 版本（[Android 版本列表](https://source.android.com/source/build-numbers.html#source-code-tags-and-builds) ([CN](https://source.android.google.cn/source/build-numbers?hl=zh-cn#source-code-tags-and-builds))，[镜像站 tags 列表](http://mirrors.ustc.edu.cn/aosp/platform/manifest.git/refs/tags/)）初始化仓库，以 `android-4.0.1_r1` 为例：

```shell
# 如果提示无法连接到 gerrit.googlesource.com，可以设置 REPO_URL 环境变量：
export REPO_URL=https://gerrit-googlesource.proxy.ustclug.org/git-repo
repo init --partial-clone -u https://mirrors.ustc.edu.cn/aosp/platform/manifest -b android-4.0.1_r1
```

同步源码树（以后只需执行这条命令来同步）：

```shell
repo sync -c
```

!!! warning "并发数量"

    由于 IO 资源有限，请勿按照 Google 文档描述设置并发为 8（`-j8`）。为了保证服务质量，超过 4 并发的用户可能会被封禁。

## 以科大源为上游设置镜像站

使用以下命令初始化：

```shell
repo init -u https://mirrors.ustc.edu.cn/aosp/mirror/manifest --mirror
```

使用以下命令同步：

```shell
repo sync
```

在内网环境下可以启用使用明文 git 协议（TCP 9418）的 git-daemon，其他用户使用 `git://your_mirror` 同步即可：

```shell
git daemon --verbose --export-all --base-path=WORKING_DIR WORKING_DIR
```

如果需要配置 Git over SSH 或 Git over HTTPS，请参考 [Git Book 4.4 到 4.6 章节的内容](https://git-scm.com/book/en/v2/Git-on-the-Server-Setting-Up-the-Server)。

## 已有仓库如何改用科大源 {#change_to_ustc}

如果您已经从官方同步了 AOSP 仓库，现在希望使用科大的 AOSP 仓库，请在 AOSP 根目录执行以下命令：

```shell
git -C ./.repo/manifests.git/ remote set-url origin https://mirrors.ustc.edu.cn/aosp/platform/manifest.git
```

## 使用时间段与并发设置建议

1. 本镜像每天凌晨 04:30 同步一次。同步可能需要较长时间，因此使用本镜像时建议避开凌晨 04:30 ～ 06:00 这段时间。
2. 由于硬盘 I/O 资源有限，请勿使用 `-j` 参数增加并发连接数到 4 个以上。`repo sync` 命令默认使用 4 个并发连接。

## 相关链接

Android 开源项目官网

:   <https://source.android.com/>

Android 开源项目官网 (CN)

:   <https://source.android.google.cn/>

Android Code Search

:   <https://cs.android.com/>
