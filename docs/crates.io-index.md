# Rust Crates

## 地址

<https://mirrors.ustc.edu.cn/crates.io-index/>

## 说明

Rust Crates Registry 源

## 使用说明

如果正在使用 cargo 1.68 及以上版本，在 `$CARGO_HOME/config.toml` 中添加如下内容即可：

```toml
[source.crates-io]
replace-with = 'ustc'

[source.ustc]
registry = "sparse+https://mirrors.ustc.edu.cn/crates.io-index/"

[registries.ustc]
index = "sparse+https://mirrors.ustc.edu.cn/crates.io-index/"
```

!!! note

    `$CARGO_HOME` 在 Windows 系统默认为：`%USERPROFILE%\.cargo`，在类 Unix 系统默认为：`$HOME/.cargo`

在 Linux 环境可以使用下面的命令完成：

```shell
mkdir -vp ${CARGO_HOME:-$HOME/.cargo}

cat << EOF | tee -a ${CARGO_HOME:-$HOME/.cargo}/config.toml
[source.crates-io]
replace-with = 'ustc'

[source.ustc]
registry = "sparse+https://mirrors.ustc.edu.cn/crates.io-index/"

[registries.ustc]
index = "sparse+https://mirrors.ustc.edu.cn/crates.io-index/"
EOF
```

!!! note "cargo <= 1.68?"

    如果 cargo 版本低于 1.68，则必须设置为完整克隆仓库，`[source.ustc]` 里的 `registry` 需要修改为：

    ```toml
    [source.ustc]
    registry = "git://mirrors.ustc.edu.cn/crates.io-index"

    # 或者如果无法使用 git 协议
    [source.ustc]
    registry = "https://mirrors.ustc.edu.cn/crates.io-index/"
    ```

    完整克隆仓库速度**远慢于**新版的稀疏索引，因此**强烈建议升级 cargo 版本**。详见[相关镜像](#related-mirrors)。

!!! note "cargo <= 1.38?"

    如果正在使用的 cargo 版本低于 1.38，则需要修改的文件为 `config` 文件，而不是 `config.toml` 文件。

!!! warning

    `cargo search` 与 `cargo info` 命令需要添加 `--registry ustc` 参数，例如：

    ```console
    cargo search --registry ustc reqwest
    cargo info --registry ustc reqwest
    ```

!!! warning

    若使用 crates 源时出现 `Couldn't resolve host name (Could not resolve host: crates)` 错误（见 <https://github.com/ustclug/discussions/issues/294>），可能需要在运行 `cargo` 的时候加入环境变量 `CARGO_HTTP_MULTIPLEXING=false`。

!!! warning

    Windows 用户在使用 crates 源时可能会出现 `next InitializeSecurityContext failed: Unknown error` 错误（见 <https://github.com/ustclug/discussions/issues/339> 和 <https://github.com/rust-lang/cargo/issues/7096>）。一个 workaround 是在运行 `cargo` 的时候加入环境变量 `CARGO_HTTP_CHECK_REVOKE=false`，或者在配置中增加：

        [http]
        check-revoke = false

## 相关镜像 {#related-mirrors}

- [Rust Toolchain 反向代理](./rust-static.md)

## 相关链接

官方主页

:   <https://crates.io/>
