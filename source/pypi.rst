===================
PyPI 镜像源使用帮助
===================

地址
====

https://mirrors.nju.edu.cn/pypi/

说明
====

PyPI(pip) 软件源

使用说明
========

编辑 ``pip`` 配置文件，将 ``index-url`` 修改为 ``https://mirrors.nju.edu.cn/pypi/web/simple`` 。

``pip`` 的配置文件一般位于（如果没有，请直接创建）：

* Unix 环境: :file:`$HOME/.config/pip/pip.conf`
* macOS: :file:`$HOME/Library/Application Support/pip/pip.conf`
* Windows: :file:`%APPDATA%\\pip\\pip.ini`

全局或者 ``virtualenv`` 等的 ``pip`` 配置文件位置，请参考 https://pip.pypa.io/en/stable/user_guide/#configuration

:file:`pip.conf` 文件配置示例如下：

::

    [global]
    index-url = https://mirrors.nju.edu.cn/pypi/web/simple
    format = columns

使用 ``pip`` 时如果出现 ``configparser.MissingSectionHeaderError: File contains no section headers.``,
说明你的 ``pip.conf`` 忘记加上 ``[global]`` 这一行了。

同步方式
========

使用 bandersnatch，从 pypi.python.org 官方同步。

相关链接
========

:pip: https://pip.pypa.io/
:bandersnatch: https://pypi.python.org/pypi/bandersnatch
