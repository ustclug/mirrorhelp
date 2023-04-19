=======================
Nix Channels 源使用帮助
=======================

地址
====

https://mirrors.ustc.edu.cn/nix-channels/

说明
====

Nixpkgs channel 以及 binary cache。为节省磁盘空间，目前设置为保留 14 天内的 channel releases 及其相关 cache。

使用说明
========

替换 channel 为科大源
^^^^^^^^^^^^^^^^^^^^^

单独安装的 Nix 对应使用的是 nixpkgs。以 ``nixpkgs-unstable`` 为例：

::

    $ nix-channel --add https://mirrors.ustc.edu.cn/nix-channels/nixpkgs-unstable nixpkgs
    $ nix-channel --update

NixOS channel 也可以以类似命令替换，以 ``nixos-19.09`` 为例（需要以 root 用户身份执行）：

::

    # nix-channel --add https://mirrors.ustc.edu.cn/nix-channels/nixos-19.09 nixos
    # nix-channel --update


替换 binary cache 为科大源
^^^^^^^^^^^^^^^^^^^^^^^^^^

对于单独安装的 Nix，需要修改或添加相应的配置（``~/.config/nix/nix.conf`` 或 ``/etc/nix/nix.conf``），配置在重启 nix-daemon 服务之后生效：

::

    substituters = https://mirrors.ustc.edu.cn/nix-channels/store https://cache.nixos.org/

对于 NixOS 和 nix-darwin，需要编辑 NixOS / nix-darwin 配置文件，系统会自动生成对应的 ``/etc/nix/nix.conf`` 文件。

.. attention::
    如果你手动指定了 ``NIX_PATH`` 或是使用 Flakes 管理系统，请根据具体情况编辑对应的文件，以下仅供参考。

对于 nix-darwin，在 ``~/.nixpkgs/darwin-configuration.nix`` 中添加：

::

    nix.binaryCaches = [ "https://mirrors.ustc.edu.cn/nix-channels/store" ];

对于 NixOS 21.11 及之前的版本，在 ``/etc/nixos/configuration.nix`` 中添加：

::

    nix.binaryCaches = [ "https://mirrors.ustc.edu.cn/nix-channels/store" ];

对于 NixOS 22.05 及之后的版本，在 ``/etc/nixos/configuration.nix`` 中添加：

::

    nix.settings.substituters = [ "https://mirrors.ustc.edu.cn/nix-channels/store" ];

.. note::
    对于所有 NixOS 19.09 及之后的版本和 nix-darwin， ``"https://cache.nixos.org/"`` 会被自动添加到配置中。

临时使用
^^^^^^^^

在安装 NixOS 时，添加 `--option substituters` 可以临时使用科大源：

::

    # nixos-install --option substituters https://mirrors.ustc.edu.cn/nix-channels/store

同样，在 NixOS 切换配置时也可以设置为临时使用：

::

    # nixos-rebuild --option substituters https://mirrors.ustc.edu.cn/nix-channels/store

将 ``substituters`` 后的参数设置为空字符串 ``""`` 可以临时禁用自己设置的镜像。

本帮助参考了 `TUNA 的 nix 帮助 <https://mirrors.tuna.tsinghua.edu.cn/help/nix/>`_ 编写。

相关链接
========

:NixOS 主页: https://nixos.org/
:安装 Nix: https://nixos.org/manual/nix/stable/installation/installing-binary.html
:上游 Nix Channels 列表: https://channels.nixos.org/
