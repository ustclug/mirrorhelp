=====================
Emacs ELPA 源使用帮助
=====================

地址
====

https://mirrors.ustc.edu.cn/elpa/

说明
====

Emacs ELPA 源。包括以下 ELPA 仓库：

- GNU ELPA
- MELPA 及 MELPA Stable
- Org

使用说明
========

在 Emacs 配置文件中（任何用到 ``package`` 特性的代码之前）添加如下内容：

::

   (setq package-archives '(("gnu" . "https://mirrors.ustc.edu.cn/elpa/gnu/")
                            ("melpa" . "https://mirrors.ustc.edu.cn/elpa/melpa/")
                            ("melpa-stable" . "https://mirrors.ustc.edu.cn/elpa/melpa-stable/")
                            ("org" . "https://mirrors.ustc.edu.cn/elpa/org/")))

或使用 Customize 功能修改 ``Package Archives`` 选项为上述内容。

相关链接
========

:Emacs 官方网站: https://www.gnu.org/software/emacs/
:Emacs Packages 文档: https://www.gnu.org/software/emacs/manual/html_node/emacs/Packages.html
