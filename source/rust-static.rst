===============================
Rust Toolchain 反向代理使用帮助
===============================

说明
====

Rust Toolchain 反向代理

使用说明
========

请配合 `rustup <http://www.rustup.rs/>`_ 来使用.

rustup 安装方法可参考官方的 `README <https://github.com/rust-lang-nursery/rustup.rs#other-installation-methods>`_

使用 rustup 前, 先设置环境变量 ``RUSTUP_DIST_SERVER`` (用于更新 toolchain):

::

    export RUSTUP_DIST_SERVER=https://mirrors.ustc.edu.cn/rust-static

以及 ``RUSTUP_UPDATE_ROOT`` (用于更新 rustup):

::

    export RUSTUP_UPDATE_ROOT=https://mirrors.ustc.edu.cn/rust-static/rustup
