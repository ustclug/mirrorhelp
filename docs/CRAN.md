# CRAN

## 地址

<https://mirrors.ustc.edu.cn/CRAN/>

## 使用说明

在第一次执行 `install.packages("xxx")` 时会弹出窗口让你选择镜像，此时选择 China (Hefei) 即可。

也可以通过 `chooseCRANmirror()` 来打开窗口，或者
`options(repos = c(USTC="https://mirrors.ustc.edu.cn/CRAN/"))`
这个选项来开启 USTC 镜像。

如果不希望每次打开 R 都必须选择镜像，可以修改 `$R_home/library/base/R/Rprofile` 文件的第 28 行（`$R_home` 可以在 R 中执行 `R.home()` 得到），将

```r
# options(repos = c(CRAN="@CRAN@"))
```

替换为

```r
options(repos = c(USTC="https://mirrors.ustc.edu.cn/CRAN/"))
```

在 Linux 系统下，普通用户可能没有 `$R_home` 目录的修改权限，此时可以执行：

```console
echo 'options(repos=c(USTC="https://mirrors.ustc.edu.cn/CRAN/"))' >> ~/.Rprofile
```

以设置当前登录用户的 R 镜像。

## 相关链接

- 官方主页： <http://cran.r-project.org/>
- FAQ： <http://cran.r-project.org/faqs.html>
- 文档： <http://cran.r-project.org/doc/>
