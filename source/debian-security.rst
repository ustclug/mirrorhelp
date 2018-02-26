==========================
Debian Security 源使用帮助
==========================

地址
====

https://mirrors.nju.edu.cn/debian-security/

说明
====

Debian 软件安全更新源

收录架构
========

Debian 支持的所有架构，如 AMD64 (x86_64), Intel x86, ARM, MIPS, ppc64el, s390x 等


收录版本
========

Debian Old Old Stable, Old Stable, Stable

当前 Stable 为 Debian 9，代号为 Stretch

使用说明
========

.. warning::
    操作前请做好相应备份

一般情况下，将 :file:`/etc/apt/sources.list` 文件中 Debian 默认的源地址 ``http://security.debian.org/``
替换为 ``http://mirrors.nju.edu.cn/debian-security/`` 即可。

可以使用如下命令：

::

  sudo sed -i 's|security.debian.org|mirrors.nju.edu.cn/debian-security|g' /etc/apt/sources.list

当然也可以直接编辑 :file:`/etc/apt/sources.list` 文件（需要使用 sudo）。以下是 Debian Stable 参考配置内容：

::

    deb http://mirrors.nju.edu.cn/debian-security/ stable/updates main non-free contrib
    # deb-src http://mirrors.nju.edu.cn/debian-security/ stable/updates main non-free contrib

更改完 :file:`sources.list` 文件后请运行 ``sudo apt-get update`` 更新索引以生效。

.. tip::
    使用 HTTPS 可以有效避免国内运营商的缓存劫持，但需要事先安装 ``apt-transport-https`` (Debian Buster
    及以上版本不需要)。


相关链接
========

:官方主页: https://www.debian.org/security/
:Debian 安全追踪网: https://security-tracker.debian.org/tracker/
