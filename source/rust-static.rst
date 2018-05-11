===============================
Rust Toolchain 反向代理使用帮助
===============================

说明
====

Rust Toolchain 反向代理

使用说明
========

请配合 `rustup <http://www.rustup.rs/>`_ 来使用。

rustup 安装方法可参考官方的 `文档 <https://github.com/rust-lang-nursery/rustup.rs#other-installation-methods>`_

使用 rustup 前，先设置环境变量 ``RUSTUP_DIST_SERVER`` （用于更新 toolchain）：

::

    export RUSTUP_DIST_SERVER=https://mirrors.ustc.edu.cn/rust-static

以及 ``RUSTUP_UPDATE_ROOT`` （用于更新 rustup）：

::

    export RUSTUP_UPDATE_ROOT=https://mirrors.ustc.edu.cn/rust-static/rustup

.. attention::
    截止到该页面编写的时候（2017-01-05）， cargo 的软件包依然托管在 AWS 上， 因此无法对下载地址做替换，
    下载速度可能较慢。但该软件包只有大概 10 MB 左右，影响不会很大。

.. note::
    第一次安装 rustup 的时候，如果安照官网教程 https://sh.rustup.rs 链接无法下载，可以通过
    `jsdelivr <https://cdn.jsdelivr.net/gh/rust-lang-nursery/rustup.rs/rustup-init.sh>`_ 下载 ``rustup-init.sh``，
    然后把脚本中的 ``RUSTUP_UPDATE_ROOT`` 变量改为 ``https://mirrors.ustc.edu.cn/rust-static/rustup``。
