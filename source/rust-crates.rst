========================
Rust Crates 镜像使用帮助
========================

地址
====

https://mirrors.ustc.edu.cn/crates.io-index/

说明
====

Rust Crates Registry 镜像

使用说明
========

在 :file:`$HOME/.cargo/config` 中添加如下内容:

::

    [source.crates-io]
    replace-with = 'ustc'

    [source.ustc]
    registry = "git://mirrors.ustc.edu.cn/crates.io-index"

如果所处的环境中不允许使用 git 协议, 可以把上述地址改为:

::

    registry = "http://mirrors.ustc.edu.cn/crates.io-index"

同步频率为每两个小时更新一次

相关链接
========

:官方主页: https://crates.io/
