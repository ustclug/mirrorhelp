=====================
Emacs ELPA 源使用帮助
=====================

地址
====

https://mirrors.ustc.edu.cn/elpa/

说明
====

Emacs ELPA 源。包括以下 ELPA 仓库：

- GNU ELPA 和 NonGNU ELPA
- MELPA 及 MELPA Stable

使用说明
========

在 Emacs 配置文件中（任何用到 ``package`` 特性的代码之前）添加如下内容：

::

   (setq package-archives '(("gnu" . "https://mirrors.ustc.edu.cn/elpa/gnu/")
                            ("melpa" . "https://mirrors.ustc.edu.cn/elpa/melpa/")
                            ("nongnu" . "https://mirrors.ustc.edu.cn/elpa/nongnu/")))

或使用 Customize 功能修改 ``Package Archives`` 选项为上述内容。

Spacemacs 使用说明
==================

添加下面的代码到 ``.spacemacs`` 的 ``dotspacemacs/user-init`` 中：

::

   (setq configuration-layer--elpa-archives
         '(("melpa-cn" . "https://mirrors.ustc.edu.cn/elpa/melpa/")
           ("nongnu-cn"   . "https://mirrors.ustc.edu.cn/elpa/nongnu/")
           ("gnu-cn"   . "https://mirrors.ustc.edu.cn/elpa/gnu/")))

develop 分支应使用 ``configuration-layer-elpa-archives`` 代替上面代码中的 ``configuration-layer--elpa-archives`` （ ``--`` 换成 ``-`` ）。

注意事项
========

由于 Emacs 的 BUG，URL 末尾的 ``/`` 不可略去，否则无法正常工作。

相关链接
========

:Emacs 官方网站: https://www.gnu.org/software/emacs/
:Emacs Packages 文档: https://www.gnu.org/software/emacs/manual/html_node/emacs/Packages.html
