===================
Stackage 源使用帮助
===================

地址
====

https://mirrors.nju.edu.cn/stackage/

说明
====

Stackage 镜像

使用说明
========

编辑 ``~/.stack/config.yaml``, 增加下列配置

::
    
    setup-info: "http://mirrors.nju.edu.cn/stackage/stack-setup.yaml"
    urls:
      latest-snapshot: http://mirrors.nju.edu.cn/stackage/snapshots.json
      lts-build-plans: http://mirrors.nju.edu.cn/stackage/lts-haskell/
      nightly-build-plans: http://mirrors.nju.edu.cn/stackage/stackage-nightly/

推荐搭配NJU Hackage源使用: :doc:`hackage`

相关链接
========

:官方主页: https://www.stackage.org/
:Stack: https://docs.haskellstack.org/en/stable/README/
