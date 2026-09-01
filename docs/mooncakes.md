# Mooncakes

## 地址

- 软件源：<https://mirrors.ustc.edu.cn/mooncakes/>
- Git 索引：<https://mirrors.ustc.edu.cn/mooncakes.git/>

## 说明

mooncakes.io（MoonBit 包管理器）的软件源。

## 使用说明

编辑 `~/.moon/config.json`（文件不存在则新建），添加或修改为如下内容：

```json
{
  "registry": "https://mirrors.ustc.edu.cn/mooncakes",
  "index": "https://mirrors.ustc.edu.cn/mooncakes.git",
  "symbols": "https://mirrors.ustc.edu.cn/mooncakes/symbols.zip"
}
```

!!! note "配置文件位置"

    配置文件位于用户主目录下的 `.moon` 目录：类 Unix 为 `$HOME/.moon/config.json`，Windows 为 `%USERPROFILE%\.moon\config.json`。若设置了环境变量 `MOON_HOME`，则位于 `$MOON_HOME/config.json`。

保存后更新本地索引：

```shell
moon update
```

!!! warning "不要使用 `MOONCAKES_REGISTRY` 环境变量"

    设置该环境变量时，`moon` 会将索引地址推导为 `$MOONCAKES_REGISTRY/git/index`，而该地址在镜像上并不存在。请通过上述 `config.json` 的方式启用本镜像。

## 相关链接

mooncakes.io

:   <https://mooncakes.io/>

MoonBit

:   <https://www.moonbitlang.com/>
