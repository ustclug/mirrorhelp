===================
Rubygems 源使用帮助
===================

地址
====

https://mirrors.ustc.edu.cn/rubygems/

说明
====

Rubygems 仓库镜像

使用说明
========

修改 Rubygems 默认源
--------------------

::

    gem sources  #列出默认源
    gem sources --remove https://rubygems.org/  #移除默认源
    gem sources -a https://mirrors.ustc.edu.cn/rubygems/  #添加科大源

针对使用 Gemfile 和 Bundle 的项目
-------------------------------------

参考： `Gem Source Mirrors @ Bundle Docs <http://bundler.io/v1.5/bundle_config.html#gem-source-mirrors-1>`_

::

    bundle config mirror.https://rubygems.org https://mirrors.ustc.edu.cn/rubygems/

相关链接
========

:官方主页: https://rubygems.org/
