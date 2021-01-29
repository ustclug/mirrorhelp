=======================
Nix Channels 源使用帮助
=======================

地址
====

https://mirrors.ustc.edu.cn/nix-channels/

说明
====

Nixpkgs channel 以及 binary cache。为节省磁盘空间，目前设置为保留半年（180 天）内的 channel 和 cache。

使用说明
========

替换 channel 为科大源
^^^^^^^^^^^^^^^^^^^^^

单独安装的 Nix 对应使用的是 nixpkgs。以 ``nixpkgs-unstable`` 为例：

::

    $ nix-channel --add https://mirrors.ustc.edu.cn/nix-channels/nixpkgs-unstable nixpkgs
    $ nix-channel --update

NixOS channel 也可以以类似命令替换，以 ``nixos-19.09`` 为例：

::

    $ nix-channel --add https://mirrors.ustc.edu.cn/nix-channels/nixos-19.09 nixos
    $ nix-channel --update


替换 binary cache 为科大源
^^^^^^^^^^^^^^^^^^^^^^^^^^

需要修改或添加相应的配置（``~/.config/nix/nix.conf`` 或 ``/etc/nix/nix.conf``）。

对于单独安装的 Nix：

::

    substituters = https://mirrors.ustc.edu.cn/nix-channels/store https://cache.nixos.org/

对于 NixOS 与 nix-darwin：

::

    nix.binaryCaches = [ "https://mirrors.ustc.edu.cn/nix-channels/store" "https://cache.nixos.org/" ];

.. tip::
    如果使用 NixOS 19.09 之后的版本和 nix-darwin，配置中的 ``"https://cache.nixos.org/"`` 可以省略。

本帮助参考了 `TUNA 的 nix 帮助 <https://mirrors.tuna.tsinghua.edu.cn/help/nix/>`_ 编写。

相关链接
========

:Nix 主页: https://nixos.org/nix
:Nixpkgs 主页: https://nixos.org/nixpkgs
:NixOS 主页: https://nixos.org/
:安装 Nix: https://nixos.org/nix/manual/#ch-installing-binary
:上游 Nix Channels 列表: https://channels.nixos.org/