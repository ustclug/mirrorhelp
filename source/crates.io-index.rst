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
    使用 nightly 版本时，Crates 源可能会出现 :code:`Couldn't resolve host name (Could not resolve host: crates)` 错误（见 https://github.com/ustclug/discussions/issues/294）。一个临时的解决方法是在运行 :code:`cargo` 的时候加入环境变量 :code:`CARGO_HTTP_MULTIPLEXING=false`。

在 :file:`$HOME/.cargo/config` 中添加如下内容：

::

    [source.crates-io]
    replace-with = 'ustc'

    [source.ustc]
    registry = "git://mirrors.ustc.edu.cn/crates.io-index"

如果所处的环境中不允许使用 git 协议，可以把上述地址改为：

::

    registry = "https://mirrors.ustc.edu.cn/crates.io-index"

.. warning::
    ``cargo search`` 无法使用镜像。

相关链接
========

:官方主页: https://crates.io/
