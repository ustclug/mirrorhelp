---
icon: material/home
---

# [中国科学技术大学开源软件镜像](/)使用帮助

GitHub 仓库：[:octicons-mark-github-16: {{ config.repo_name }}]({{ config.repo_url }})。有关本帮助的问题，可在仓库中创建 issue 或提交 PR。

部分帮助内容修改自 [教育网联合镜像站帮助](https://help.mirrors.cernet.edu.cn/)（CC BY-NC-SA 4.0 许可协议）。

提示：可以按下 ++s++ 键开始搜索。

!!! info "信息"

    {% if git.status %}
    本帮助页面部署自 [`{{ git.short_commit }}` {{ git.author }}: {{ git.message.split('\n')[0] }}]({{ config.repo_url }}/commit/{{ git.commit }})。
    {% else %}
    本帮助页面好像不是从 Git 仓库部署的？
    {% endif %}

    更新时间：{{ now().strftime("%Y-%m-%d %H:%M:%S") }}
