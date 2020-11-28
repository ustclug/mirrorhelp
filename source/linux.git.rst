==================
Linux 内核源码镜像
==================

其 Git 仓库的链接为 ``git://mirrors.ustc.edu.cn/linux.git`` 与 ``https://mirrors.ustc.edu.cn/linux.git``。

断点续传
--------

由于 ``git clone`` 不支持断点续传，所以可以使用支持断点续传的 ``git fetch``。一个简单的步骤如下所示，请按自己的需求酌情更改：

::

   mkdir linux && cd linux
   git init
   git fetch git://mirrors.ustc.edu.cn/linux.git
   git checkout FETCH_HEAD