=================
CRAN 镜像使用帮助
=================

使用说明
========

在第一次执行 ``install.package("xxx")`` 时会弹出窗口让你选择镜像，此时选择
China Hefei 即可。

也可以通过 ``chooseCRANmirror()`` 来打开窗口，或者 ``options(repos = c(USTC="https://mirrors.ustc.edu.cn/CRAN/"))`` 这个选项来开启USTC镜像。


我们可以修改`$R_home/library/base/R/Rprofile`文件的第(28)行：
将
```
# options(repos = c(CRAN="@CRAN@"))
```
替换为
```
options(repos = c(USTC="https://mirrors.ustc.edu.cn/CRAN/"))
```

相关链接
========

-  官方主页： http://cran.r-project.org/

-  FAQ： http://cran.r-project.org/faqs.html

-  文档： http://cran.r-project.org/doc/
