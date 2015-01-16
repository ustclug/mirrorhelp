mirrorhelp
==========

介绍
--------

这里是[中科大开源镜像站](https://mirrors.ustc.edu.cn/)镜像使用帮助文档的源文件。
文档以 Markdown 格式与 DokuWiki 格式混合写成，请在[这里](https://lug.ustc.edu.cn/wiki/mirrors/help)访问已排版的文档。

欢迎各位协助完善文档内容。你可以采用[DokuWiki 语法](https://www.dokuwiki.org/zh:syntax)
或者[Markdown 语法](http://wowubuntu.com/markdown/)进行写作，我们的网站能够进行混合排版。

如果您有对本文档，或是对镜像站资源的疑问、意见或建议，请向我们的邮箱: lug (at) ustc.edu.cn
发送邮件，或是在这里提交一个 issue.

写作规范
-----------

-  每一篇文档的文件名都应当以`.txt`结尾。
-  对一些特殊字符，如`_`和` *`，应当在其前面加上`\`进行转义。
-  请为每篇文档添加一个与 HTML 中`h1`标签相对等的标题。例如，在文档第一行写下`====== Distro 镜像源使用帮助 ======`(DokuWiki 语法)，或者写下`# Distro 镜像源使用帮助 #`(Markdown 语法)。
-  配置文件、脚本等文本文件可以使用`<file>`标签，并配以适当的属性说明，如`.ini`, `.sh`或`.repo`，以实现自动语法高亮。作为例子，你可以参考 Anthon 镜像源使用帮助文档源文件的写作样式。
-  对于一段较长的代码，请适当地使用`<code>`标签并另起一段。如果要使用行间代码，请使用<code>`somecode`</code>的写作方式。**写作示例**可以在[LUG Wiki Playground](https://lug.ustc.edu.cn/wiki/playground/playground)找到，供参考。
-  请在 CJK 字符和英文单词之间加上一个半角空格。
-  **不要忘记**在添加新文档后更新`help.txt`索引。

Introduction
-------------

This is the guide on using the mirrored repositories provided by mirrors.ustc.edu.cn.
Generally these are DokuWiki format text placed on https://lug.ustc.edu.cn/wiki/mirrors/help.

Contributions are always welcome. You may write text in [DokuWiki style](https://www.dokuwiki.org/wiki:syntax)
or Markdown style because we have installed the markdown plugin, and the engine matches both.
You can even combine those two types of syntax in one single document, as long as there is no conflict.

Any question, please contact us at lug (at) ustc.edu.cn or submit an issue.

Writing Rules
-----

- All files should have a filename ended with .txt.
- Some special characters, such as `_` and ` *`, should be escaped with a backslash `\`, so it looks like `\_` and `\*` in the source text, since we have a mixed parsing engine of DokuWiki and Markdown.
- All page titles should be `h1` in the resulting HTML. So the title should be something like `====== Distro 镜像源使用帮助 ======` in DokuWiki syntax.
- Configuration files and other attachments should be wrapped inside a `<file>` tag with a corresponding syntax, like `ini` for `.repo` files. Code blocks should be highlighted, too.
- Paths should be wrapped in a `<code>` tag in the resulting HTML. Use <code>\`/path/to/file\`</code> for this. Inline code, like commands, should be treated in the same way. For a quick example, check [LUG Wiki Playground](https://lug.ustc.edu.cn/wiki/playground/playground).
- There should be a space between CJK and English or other western text.
- Lists should be using the corresponding tags in the resulting HTML. 
- **Always** add new help entries to `help.txt`.

* * *
LUG@USTC

