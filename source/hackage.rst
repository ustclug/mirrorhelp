==================
Hackage 源使用帮助
==================

地址
====

https://mirrors.ustc.edu.cn/hackage/

说明
====

Hackage 镜像

stack使用说明
=============

编辑~/.stack/config.yaml, 增加下列参数

::

    package-indices:
      - name: USTC
        download-prefix: https://mirrors.ustc.edu.cn/hackage/package/
        http: https://mirrors.ustc.edu.cn/hackage/00-index.tar.gz


cabal使用说明
=============

.. todo:: cabal使用说明


相关链接
========

:官方主页: https://hackage.haskell.org/
