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

## 同步方式

- 软件包元数据使用 shadowmire 从 TUNA 同步
- 软件包根据访问情况进行动态缓存，未命中的包重定向到 TUNA

## 相关链接

pip

:   <https://pip.pypa.io/>

shadowmire

:   <https://github.com/taoky/shadowmire/>
