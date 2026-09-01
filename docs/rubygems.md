# RubyGems

## 地址

<https://mirrors.ustc.edu.cn/rubygems/>

## 说明

RubyGems 仓库镜像，目前为缓存。

## 使用说明

### 修改 RubyGems 默认源

```shell
gem sources # 列出默认源
gem sources --remove https://rubygems.org/ # 移除默认源
gem sources -a https://mirrors.ustc.edu.cn/rubygems/ # 添加科大源
```

### 针对使用 Gemfile 和 Bundle 的项目

参考 [Mirrors Of Gem Sources](https://guides.rubygems.org/command-reference/bundle-config/)：

```shell
bundle config set --global mirror.https://rubygems.org https://mirrors.ustc.edu.cn/rubygems/
```

## 相关链接

官方主页

:   <https://rubygems.org/>
