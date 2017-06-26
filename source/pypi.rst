===========================
PyPI 镜像源使用帮助
===========================

地址
====

https://mirrors.ustc.edu.cn/pypi/

说明
====

PyPI(pip) 软件源.


使用说明
========

编辑 ~/.pip/pip.conf 文件（如果没有则创建之），将 index-url 开头的一行修改为下面一行：

::

    index-url = https://mirrors.ustc.edu.cn/pypi/web/simple
  
如果运行 pip 时, 提示如下错误:

::
    configparser.MissingSectionHeaderError: File contains no section headers.
  
请在 ~/.pip/pip.conf 最上方加上 [global] 这一 section header

如：

::

    [global]
    index-url = https://mirrors.ustc.edu.cn/pypi/web/simple
    format = columns

同步方式
========

使用 bandersnatch，每4小时从 pypi.python.org 官方同步。



相关链接
========
:PyPI Official Mirrors: https://pypi.python.org/mirrors
:PEP-381 Mirroring Protocol: http://www.python.org/dev/peps/pep-0381/
:bandersnatch: https://pypi.python.org/pypi/bandersnatch
