# openEuler

## 地址

<https://mirrors.ustc.edu.cn/openeuler/>

## 说明

openEuler 软件源

## 收录架构

x86_64, aarch64

## 收录版本

20.03-LTS, 20.09, 21.03, 21.09, 22.03-LTS, 22.09, 23.03, 23.09, 24.03-LTS, 24.09

## 使用说明

!!! warning

    操作前请做好相应备份。

使用以下命令替换默认配置

```shell
sudo sed -E 's#https?://(repo|mirrors)\.openeuler\.org/#https://mirrors.ustc.edu.cn/openeuler/#g' \
         -i.bak \
         /etc/yum.repos.d/openEuler.repo
```

以上命令替换了所有的仓库。替换之后请运行 `yum makecache` 更新缓存。

## 相关链接

官方主页

:   <https://www.openeuler.org/>

邮件列表

:   <https://www.openeuler.org/zh/community/mailing-list/>

论坛

:   <https://forum.openeuler.org/>

文档

:   <https://docs.openeuler.org/zh/>

镜像列表

:   <https://www.openeuler.org/zh/mirror/list/>
