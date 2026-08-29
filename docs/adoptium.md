# Adoptium

## 地址

<https://mirrors.ustc.edu.cn/adoptium/>

## Windows/macOS 用户
通过以下链接打开下载页面，选择所需的版本，下载独立安装包。

https://unicom.mirrors.ustc.edu.cn/adoptium/releases/

## Debian/Ubuntu 用户

首先请安装依赖：
```shell
sudo apt-get update && sudo apt-get install -y wget apt-transport-https
```

然后信任 GPG 公钥：
```shell
wget -O - https://packages.adoptium.net/artifactory/api/gpg/key/public | sudo tee /etc/apt/keyrings/adoptium.asc
```

随后执行以下命令来添加 apt 存储库：
```shell
echo "deb [signed-by=/etc/apt/keyrings/adoptium.asc] https://mirrors.ustc.edu.cn/adoptium/deb $(awk -F= '/^VERSION_CODENAME/{print$2}' /etc/os-release) main" | sudo tee /etc/apt/sources.list.d/adoptium.list
```
再执行
```shell
sudo apt-get update
```

之后可以使用 `apt-get install temurin-<version>-jdk` 安装软件包，例如 `temurin-17-jdk` 和 `temurin-8-jdk`。