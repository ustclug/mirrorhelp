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

编辑 ``~/.stack/config.yaml``, 增加下列参数

::

    package-indices:
      - name: USTC
        download-prefix: https://mirrors.ustc.edu.cn/hackage/package/
        http: https://mirrors.ustc.edu.cn/hackage/01-index.tar.gz


cabal使用说明
=============

1. 执行 ``cabal user-config init``
2. 修改 ``~/.cabal/config``

Cabal ≥ 1.24 (GHC 8.0)
----------------------
找到官方仓库:
::

    repository hackage.haskell.org
      url: http://hackage.haskell.org/
      -- secure: True
      -- root-keys:
      -- keys-threshold: 3

改为科大源:
::

    repository mirrors.ustc.edu.cn
      url: https://mirrors.ustc.edu.cn/hackage/
      secure: False

Cabal < 1.24
------------
找到官方仓库:
::

    remote-repo: hackage.haskell.org:http://hackage.haskell.org/packages/archive

改为科大源:
::

    remote-repo: mirrors.ustc.edu.cn:http://mirrors.ustc.edu.cn/hackage/

3. 执行 ``cabal update``

相关链接
========

:官方主页: https://hackage.haskell.org/
:Cabal: https://www.haskell.org/cabal/
:Stack: https://docs.haskellstack.org/en/stable/README/
