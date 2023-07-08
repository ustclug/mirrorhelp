======================
Rust Crates 源使用帮助
======================

地址
====

https://mirrors.ustc.edu.cn/crates.io-index/

说明
====

Rust Crates Registry 源

使用说明
========

.. warning::
    若使用 crates 源时出现 :code:`Couldn't resolve host name (Could not resolve host: crates)` 错误（见 https://github.com/ustclug/discussions/issues/294），可能需要在运行 :code:`cargo` 的时候加入环境变量 :code:`CARGO_HTTP_MULTIPLEXING=false`。

.. warning::
    Windows 用户在使用 crates 源时可能会出现 :code:`next InitializeSecurityContext failed: Unknown error` 错误（见 https://github.com/ustclug/discussions/issues/339 和 https://github.com/rust-lang/cargo/issues/7096）。一个 workaround 是在运行 :code:`cargo` 的时候加入环境变量 :code:`CARGO_HTTP_CHECK_REVOKE=false`，或者在配置中增加：

    ::

        [http]
        check-revoke = false

.. note::
    cargo 1.68 版本开始支持稀疏索引：不再需要完整克隆 crates.io-index 仓库，可以加快获取包的速度。如果您的 cargo 版本大于等于 1.68，可以在 :file:`$CARGO_HOME/config` 中添加如下内容：

    ::

        [source.crates-io]
        replace-with = 'ustc'

        [source.ustc]
        registry = "sparse+https://mirrors.ustc.edu.cn/crates.io-index/"

    在 Linux 环境可以使用下面的命令完成

    ::

        mkdir -vp ${CARGO_HOME:-$HOME/.cargo}

        cat << EOF tee -a ${CARGO_HOME:-$HOME/.cargo}/config
        [source.crates-io]
        replace-with = 'ustc'

        [source.ustc]
        registry = "sparse+https://mirrors.ustc.edu.cn/crates.io-index/"
        EOF


在 :file:`$CARGO_HOME/config.toml` 中添加如下内容：

::

    [source.crates-io]
    replace-with = 'ustc'

    [source.ustc]
    registry = "git://mirrors.ustc.edu.cn/crates.io-index"

在 Linux 环境可以使用下面的命令完成

::

    mkdir -vp ${CARGO_HOME:-$HOME/.cargo}

    cat << EOF tee -a ${CARGO_HOME:-$HOME/.cargo}/config
    [source.crates-io]
    replace-with = 'ustc'

    [source.ustc]
    registry = "git://mirrors.ustc.edu.cn/crates.io-index"
    EOF

如果所处的环境中不允许使用 git 协议，可以把上述地址改为：

::

    registry = "https://mirrors.ustc.edu.cn/crates.io-index"

.. warning::
    ``cargo search`` 无法使用镜像。

相关链接
========

:官方主页: https://crates.io/
