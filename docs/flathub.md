# Flathub 缓存

Flathub 是 Flatpak 默认的软件源，包含了必需的运行时、开发者工具箱，以及基于此打包的大量应用程序。本镜像站提供 Flathub 的**缓存**。

!!! warning "测试中"
    本镜像处于测试阶段，以下内容可能发生变化。

## 同步细节

Flathub 的元数据（`config`, `summary.idx`, `summaries/`）每小时完整同步一次。

Flathub 的 blob 数据（`objects/`）与增量更新数据（`deltas/`, `delta-indexes/`）为动态缓存，根据用户访问情况，每小时更新一次。**在请求未命中时，会 302 重定向到 Flathub 源站点**。本镜像不是 Flathub 的完整镜像，因此仍然需要用户到 Flathub 站点有基本的可连通性。

软件 manifest 中标注为 `extra-data` 的文件不会经过镜像站或 Flathub 服务器，而是直接从标注的源站点下载。

## 配置方法

在已有 `flathub` 远程源的基础上：

```shell
sudo flatpak remote-modify flathub --url=https://mirrors.ustc.edu.cn/flathub
```

恢复默认值：

```shell
sudo flatpak remote-modify flathub --url=https://dl.flathub.org/repo
```

## 调试方法

如果怀疑网络问题，请添加 `OSTREE_DEBUG_HTTP=1` 环境变量后再次运行 `flatpak` 命令以获取 libcurl 的详细输出，例如：

```shell
OSTREE_DEBUG_HTTP=1 flatpak install com.github.tchx84.Flatseal
```

## 相关链接

Flathub

:   <https://flathub.org>

Flatpak

:   <https://flatpak.org>

SJTUG Flathub 智能缓存

:   <https://mirrors.sjtug.sjtu.edu.cn/docs/flathub>
