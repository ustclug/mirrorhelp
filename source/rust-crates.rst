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

在 :file:`$HOME/.cargo/config` 中添加如下内容：

::

    [registry]
    index = "git://mirrors.ustc.edu.cn/crates.io-index"


如果所处的环境中不允许使用 git 协议，可以把上述地址改为：

::

    index = "git://mirrors.ustc.edu.cn/crates.io-index"

相关链接
========

:官方主页: https://crates.io/
