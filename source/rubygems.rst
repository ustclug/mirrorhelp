==============================
Rubygems 源使用帮助
==============================

地址
====

https://mirrors.ustc.edu.cn/rubygems/

说明
====

Rubygems仓库镜像

使用说明
========

修改Rubygems默认源：
::

    gem sources  #列出默认源
    gem sources --remove https://rubygems.org/  #移除默认源
    gem sources -a https://mirrors.ustc.edu.cn/rubygems/  #添加科大源

针对使用使用Gemfile和Bundle的项目：
::

    bundle config mirror.https://rubygems.org https://mirrors.ustc.edu.cn/rubygems/

参考：`Gem Source Mirrors @ Bundle Docs <http://bundler.io/v1.5/bundle_config.html#gem-source-mirrors-1>`_

