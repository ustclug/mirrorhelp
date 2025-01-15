# Debian CN

## 地址

<https://mirrors.ustc.edu.cn/debiancn/>

## 说明

[Debian 中文社区](https://www.debiancn.org)提供了一系列软件，可作为对 Debian 官方仓库的一个补充，其目的之一是改进 Debian 中文用户在 Debian 系统上的使用体验。

## 收录范围

优先提供 `amd64` 架构的软件。有少部分软件同时提供源码包（使用 `deb-src` 启用）。少量软件提供 `i386` 等其他架构。

## 收录版本

{% for release in debian_releases %}

- {{ release.codename }}

{% endfor %}

目前暂无专用于 testing 和 sid 的仓库。

## 使用说明

!!! tip

    请参考[上游使用说明](https://github.com/debiancn/repo)并将所有 `repo.debiancn.org` 字符串替换为 `mirrors.ustc.edu.cn/debiancn` 即可。

## 相关链接

社区主页

:   <https://www.debiancn.org/>

仓库主页

:   <https://repo.debiancn.org/>

使用文档与 Git 仓库

:   <https://github.com/debiancn/repo>

其它镜像列表

:   <https://github.com/debiancn/repo/issues/60>
