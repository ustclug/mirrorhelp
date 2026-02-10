# PyPI

## 地址

<https://mirrors.ustc.edu.cn/pypi/>

## 说明

PyPI（pip）软件源

## 使用说明

### 临时使用

    pip install -i https://mirrors.ustc.edu.cn/pypi/simple package

### 设为默认

升级 `pip` 到最新的版本 `(>=10.0.0)` 后进行配置：

```shell
# 使用本镜像站来升级 pip
pip install -i https://mirrors.ustc.edu.cn/pypi/simple pip -U
pip config set global.index-url https://mirrors.ustc.edu.cn/pypi/simple
```

### 其他包管理器

#### Astral uv

添加配置文件 `~/.config/uv/uv.toml` 或 `/etc/uv/uv.toml`，内容如下：

```toml
[[index]]
url = "https://mirrors.ustc.edu.cn/pypi/simple"
default = true
```

!!! info "python-build-standalone 镜像"

    我们提供了 python-build-standalone 的镜像，详情请见 [github-release 帮助](./github-release.md#python-build-standalone)。

!!! warning "设置 index 会改变 `uv.lock` 的内容"

    详见 <https://github.com/astral-sh/uv/issues/9056> 与 <https://github.com/astral-sh/uv/issues/6349>。

    一个临时的绕过方法是，在需要将 `uv.lock` commit 到版本管理工具之前执行 `UV_INDEX=https://pypi.org/simple uv lock --refresh`，来还原 `uv.lock` 中的信息。

## 同步方式

- 软件包元数据使用 shadowmire 从 TUNA 同步
- 软件包根据访问情况进行动态缓存，未命中的包重定向到 TUNA

## 相关链接

pip

:   <https://pip.pypa.io/>

shadowmire

:   <https://github.com/taoky/shadowmire/>
