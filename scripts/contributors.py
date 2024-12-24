import os
import requests


HEADER = """\
# 文档贡献者名单

你也可以前往 <https://github.com/ustclug/mirrorhelp/graphs/contributors> 获取全部贡献者列表。

以字典序排序：

<style>
.md-typeset div.grid.cards > ul > li {
  padding: 0;
  padding-right: .8em;
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-items: center;
}

.md-typeset div.grid.cards > ul > li > img {
  margin: 0;
  border-top-left-radius: .1rem;
  border-bottom-left-radius: .1rem;
}

.md-typeset div.grid.cards > ul > li > img + a {
  margin: 0 .8em;
}
</style>
"""


def get_api():
    if "CI" not in os.environ:
        return [
            {
                "login": "（本文件由 CI 生成，参见仓库中的 `scripts/contributors.py`）",
                "html_url": "#top",
            }
        ]
    headers = {
        "User-Agent": "Python/0.0.1 (+https://github.com/ustclug/mirrorhelp/blob/master/source/contributors.py)"
    }
    if "GITHUB_TOKEN" in os.environ:
        headers["Authorization"] = f"token {os.environ['GITHUB_TOKEN']}"
    r = requests.get("https://api.github.com/repos/ustclug/mirrorhelp/contributors", headers=headers)
    r.raise_for_status()
    return r.json()


def main():
    data = get_api()
    data.sort(key=lambda x: x["login"].casefold())

    filename = os.path.abspath(os.path.join(__file__, os.path.pardir, os.path.pardir, "docs", "contributor.md"))
    with open(filename, "w") as f:
        print(HEADER, file=f)
        print('<div class="grid cards" markdown>', file=f)
        for item in data:
            print(f"- ![Avatar]({item['avatar_url']}){{: width=64 height=64 }} [{item['login']}]({item['html_url']})", file=f)
        print('</div>', file=f)


if __name__ == "__main__":
    main()
