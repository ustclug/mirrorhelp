# CentOS Stream

## 地址

<https://mirrors.ustc.edu.cn/centos-stream/>

## 说明

CentOS Stream 软件源

## 收录架构

官方支持的架构

## 收录版本

9-stream, 10-stream

## 使用说明

!!! warning

    操作前请做好相应备份。

替换以下文件：

```ini title="/etc/yum.repos.d/centos.repo"
--8<-- "centos9stream/centos.repo"
```

```ini title="/etc/yum.repos.d/centos-addons.repo"
--8<-- "centos9stream/centos-addons.repo"
```

替换之后请运行 `yum makecache` 更新缓存。
