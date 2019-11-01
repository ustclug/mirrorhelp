===================
PyPI 镜像源使用帮助
===================

.. warning::
    PyPI 源已暂时移除并重定向到 TUNA PyPI，详见 `PyPI 镜像变更通知 <https://servers.ustclug.org/2019/01/pypi-%e9%95%9c%e5%83%8f%e5%8f%98%e6%9b%b4%e9%80%9a%e7%9f%a5/>`_。

地址
====

https://mirrors.ustc.edu.cn/pypi/

说明
====

PyPI(pip) 软件源

使用说明
========

临时使用
--------

::

    pip install -i https://mirrors.ustc.edu.cn/pypi/web/simple package

设为默认
--------

升级 ``pip`` 到最新的版本 ``(>=10.0.0)`` 后进行配置：

::

    # 使用本镜像站来升级 pip
    pip install -i https://mirrors.ustc.edu.cn/pypi/web/simple pip -U
    pip config set global.index-url https://mirrors.ustc.edu.cn/pypi/web/simple

同步方式
========

使用 bandersnatch，从 pypi.python.org 官方同步。

相关链接
========

:pip: https://pip.pypa.io/
:bandersnatch: https://pypi.python.org/pypi/bandersnatch
