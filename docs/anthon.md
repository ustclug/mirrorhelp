# AOSC OS

## 地址

<https://mirrors.ustc.edu.cn/anthon>

## 说明

AOSC OS（安同 OS）软件源。AOSC OS 是一个由安同开源社区（<https://aosc.io>）开发的半滚动 Linux 发行版，支持多种处理器架构。

## 使用说明

### 工具修改

请使用以下命令交互式开启/关闭镜像源，输入镜像源名称并使用空格启用/禁用镜像源（请注意：`oma mirror` 允许指定多个镜像源，请注意禁用不需要使用的镜像源）：

```shell
sudo oma mirror
```

关于 `oma mirror` 的更多详细命令和用法，请参考 [oma 的 GitHub 页面](https://github.com/AOSC-Dev/oma?tab=readme-ov-file#command-reference)。

### 手动修改（不推荐）

安同 OS 推荐使用 `oma` 完成对软件源配置的修改，不推荐手动编辑配置文件。

如确实有相关需求，请按下例编辑 `/etc/apt/sources.list` 的内容：

```debsources
deb https://mirrors.ustc.edu.cn/anthon/debs stable main
```

## 相关链接

官方主页

:   <https://aosc.io>

文档

:   <https://wiki.aosc.io>

镜像列表

:   <https://aosc.io/repo>
