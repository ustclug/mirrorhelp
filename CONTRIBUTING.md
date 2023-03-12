# How to contribute

## Ways to improve the documents

* Submit an issue

  If you find errors in documents or want to improve, this is the easiest way to help.
  You can put your document in any format in the issue comments, then a core developer
  will format it into reStructureText syntax and commit it to the repo.

* Send a pull request

  This way is for those who are familiar with
  [Git workflow](https://guides.github.com/introduction/flow/) and
  [reStructureText](http://www.sphinx-doc.org/en/stable/rest.html).
  A PR needs to be reviewed by at least one person before merging.

## Document format

* Chinese writing guideline

  Please follow <https://github.com/sparanoid/chinese-copywriting-guidelines/blob/master/README.en-US.md>

* reStructureText syntax

  Make sure `make html` runs without errors.

  Please include a single rst file in a [TOC tree](http://www.sphinx-doc.org/en/stable/markup/toctree.html).
  For example, add a reference in `index.rst`.

## Environment setup

1. Create a virtual environment

    ```bash
    python3 -m venv .env
    ```
2. Activate the virtual environment

    ```bash
    # bash
    source .env/bin/activate
    # fish
    source .env/bin/activate.fish
    ```
3. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```
4. Build the documents

    ```bash
    make html
    ```
5. Open the documents

    ```bash
    # macOS/fish
    open build/html/index.html
    # Linux
    xdg-open build/html/index.html
    ```

## Credit

For those who improved the documents, the GitHub username will be mentioned in the
[document](https://mirrors.ustc.edu.cn/help/contributor.html).


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

  请参考 <https://github.com/sparanoid/chinese-copywriting-guidelines>。

* reStructureText 格式

  `make html` 会检查语法，请确保运行结果没有错误。

  单个 rst 文件需要被包含在 [TOC tree](http://www.sphinx-doc.org/en/stable/markup/toctree.html) 中，例如可以在 `index.rst` 文件中添加索引。

## 环境配置

1. 创建虚拟环境

    ```bash
    python3 -m venv .env
    ```
2. 激活虚拟环境

    ```bash
    # bash
    source .env/bin/activate
    # fish
    source .env/bin/activate.fish
    ```
3. 安装依赖

    ```bash
    pip install -r requirements.txt
    ```
4. 构建帮助文档

    ```bash
    make html
    ```
5. 查看构建的帮助文档

    ```bash
    # macOS/fish
    open build/html/index.html
    # Linux
    xdg-open build/html/index.html
    ```

## 署名

参与任何形式的贡献，相关的 GitHub 用户名会在[文档](https://mirrors.ustc.edu.cn/help/contributor.html)中提及。
