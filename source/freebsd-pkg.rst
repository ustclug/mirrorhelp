========================
FreeBSD pkg 源使用帮助
========================

地址
====

http://mirrors.ustc.edu.cn/freebsd-pkg/

说明
====

FreeBSD pkg 软件源

收录架构
========

i386,amd64,aarch64,armv6,mips,mips64


收录版本
========

FreeBSD 10,FreeBSD 11,FreeBSD 12

使用方法
========
 
创建用户级pkg源目录
    
    file:`/usr/local/etc/pkg/repos`

* 新建源文件
    
    file:`/usr/local/etc/pkg/repos/1.ustc.conf`

 在``1.ustc.conf``中添加以下内容，以使用USTC源：

::

		ustc: {
		  url: "pkg+http://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/latest",
		  mirror_type: "srv",
		  signature_type: "none",
		  fingerprints: "/usr/share/keys/pkg",
		  enabled: yes
		}
	

* （建议）禁用系统级pkg源

::
	
    mv /etc/pkg/FreeBSD.conf /etc/pkg/FreeBSD.conf.back

 
然后运行 ``pkg update -f`` 更新索引以生效。 



相关链接
========

:官方主页: https://www.freebsd.org
:论坛: https://forums.freebsd.org
:文档: https://www.freebsd.org/doc
