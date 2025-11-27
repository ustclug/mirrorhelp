# Linux 内核源码

## 地址

<https://mirrors.ustc.edu.cn/linux.git>

## 断点续传

由于 `git clone` 不支持断点续传，所以可以使用支持断点续传的 `git fetch`。一个简单的步骤如下所示，请按自己的需求酌情更改：

    mkdir linux && cd linux
    git init
    git fetch https://mirrors.ustc.edu.cn/linux.git
    git checkout FETCH_HEAD

## 部分克隆

如果不需要完整的仓库历史，可以使用部分克隆来节省空间和时间。使用以下命令：

```shell
git clone --filter=tree:0 https://mirrors.ustc.edu.cn/linux.git
cd linux
```
