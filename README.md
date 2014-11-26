mirrorhelp
==========

This is the guide on using the mirrored repositories provided by mirrors.ustc.edu.cn.
Generally these are DokuWiki format text placed on https://lug.ustc.edu.cn/wiki/mirrors/help/.

Contributions are always welcome. You may write text in [DokuWiki](https://www.dokuwiki.org/zh:syntax) [style](https://www.dokuwiki.org/wiki:syntax)
or Markdown style because we have installed the markdown plugin, and the engine matches both. All text files should be txts. You can
combine those two types of syntax. Since Markdown is being parsed here, you should
escape keywords like literal `_` and ` *` with a backslash `\`, so it looks like `\_` in the source text.

Any question, please contact us at lug@ustc.edu.cn or submit an issue.

* * *
LUG@USTC

Rules
-----

- A valid mirror help page should **at least** contain basic description of the mirror and configuration files so readers can use it.
- All page titles should be `h1` in the resulting HTML. So the title should be something like `====== Distro 镜像源使用帮助 ======` in DokuWiki syntax.
- Configuration files and other attachments should be wrapped inside a `<file>` tag with a corresponding syntax, like `ini` for `.repo` files. Code blocks should be highlighted, too.
- Paths should be wrapped in a `<code>` tag in the resulting HTML. Use <code>\`/path/to/file\`</code> for this. Inline code, like commands, should be treated in the same way.
- There should be a space between CJK and English or other western text.
- Lists should be using the corresponding tags in the resulting HTML. 
- **Always** add new help entries to `help.txt`.
