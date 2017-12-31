========================
FreeBSD ports 源使用帮助
========================

地址
====

http://mirrors.ustc.edu.cn/freebsd-ports/

说明
====

FreeBSD ports 软件源

收录架构
========

所有架构


收录版本
========

所有版本

使用方法
========
 
创建或修改文件：
    
    :file:`/etc/make.conf`

在 :file:`/etc/make.conf` 中添加以下内容，以使用USTC源：

::

    MASTER_SITE_OVERRIDE?=http://mirrors.ustc.edu.cn/freebsd-ports/distfiles/


相关链接
========

:官方主页: https://www.freebsd.org
:论坛: https://forums.freebsd.org
:文档: https://www.freebsd.org/doc
