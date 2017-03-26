# How to contribute

## Ways to improve the documents

* Submit a issue

  If you find errors in documents or want to improve, this is the easiest way to help.
  You can put your document in any format in the issue comments, then a core developer
  will format it with reStructureText syntax and commit it into the repo.

* Send a pull request

  This way is for those who are familar with
  [Git workflow](https://guides.github.com/introduction/flow/) and the
  [reStructureText](http://www.sphinx-doc.org/en/stable/rest.html).
  A PR needs to be reviewed by at least one person before merging.

## Document format

* Chinese writing guideline

  Follow section 3 in https://mirrors.ustc.edu.cn/anthon/aosc-l10n/zh_CN_l10n.pdf

* reStructureText syntax

  Make sure `make html` run without errors.

  Please include a single rst file in a [TOC tree](http://www.sphinx-doc.org/en/stable/markup/toctree.html).
  For example, add a reference in `index.rst`.

## Credit

For those improved the documnets, the Github username will be mentioned in the
[document](http://mirrors.ustc.edu.cn/help/contributor.html).


# 如何贡献

## 如何改善文档

* 提交 issue

  如果你发现文档中有错误，你可以在 issue 中提出。你也可以在 issue 中提交改进后的文档。
  Issue 中提交的文档可以用任何格式撰写，后面我们会把文档格式化成标准的 reStructureText 格式。

* 提交 pull request

  如果你熟悉 [Git 的协作流程](https://guides.github.com/introduction/flow/)，
  也熟悉 [reStructureText 格式](http://www.sphinx-doc.org/en/stable/rest.html)，
  请 pull request。
  注意 PR 在合并前至少需要一个人进行 review。

## 文档格式

* 中文写作规范

  请参考 https://mirrors.ustc.edu.cn/anthon/aosc-l10n/zh_CN_l10n.pdf 中的第 3 章节。

* reStructureText 格式

  `make html` 会检查语法，请确保运行结果没有错误。

  单个 rst 文件需要被包含在 [TOC tree](http://www.sphinx-doc.org/en/stable/markup/toctree.html) 中，例如可以在 `index.rst` 文件中添加索引。

## 署名

参与任何形式的贡献，相关的 Github 用户名会在[文档](http://mirrors.ustc.edu.cn/help/contributor.html)中提及。
