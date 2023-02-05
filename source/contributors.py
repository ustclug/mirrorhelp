import os
import json
import urllib.request


HEADER = """\
==============
文档贡献者名单
==============

你也可以前往 https://github.com/ustclug/mirrorhelp/graphs/contributors 获取全部贡献者列表。

以字典序排序：
"""


def get_api():
    req = urllib.request.urlopen("https://api.github.com/repos/ustclug/mirrorhelp/contributors")
    return json.load(req)


def main(app):
    filename = os.path.abspath(os.path.join(__file__, os.path.pardir, "contributor.rst"))
    with open(filename, "w") as f:
        print(HEADER, file=f)
        data = get_api()
        data.sort(key=lambda x: x["login"].casefold())
        for item in data:
            print(f"* {item['login']}", file=f)


def setup(app):
    app.connect("builder-inited", main)
