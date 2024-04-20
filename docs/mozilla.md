# Mozilla Firefox 源使用帮助

## 地址

<https://mirrors.ustc.edu.cn/mozilla/>

## 说明

Firefox Deb 包镜像

## 收录版本

AMD64 架构下的最新稳定版、beta、nightly、开发者版本与语言包。

## 使用说明

以下内容参考了 [Install Firefox on
Linux](https://support.mozilla.org/en-US/kb/install-firefox-linux#w_install-firefox-deb-package-for-debian-based-distributions)
的说明并稍作修改：

1.  创建 keyrings 目录：

```{=html}
<!-- -->
```
    sudo install -d -m 0755 /etc/apt/keyrings

2.  导入 Mozilla APT 仓库公钥：

```{=html}
<!-- -->
```
    wget -q https://packages.mozilla.org/apt/repo-signing-key.gpg -O- | sudo tee /etc/apt/keyrings/packages.mozilla.org.asc > /dev/null

3.  验证签名一致性：

```{=html}
<!-- -->
```
    gpg -n -q --import --import-options import-show /etc/apt/keyrings/packages.mozilla.org.asc | awk '/pub/{getline; gsub(/^ +| +$/,""); if($0 == "35BAA0B33E9EB396F59CA838C0BA5CE6DC6315A3") print "\nThe key fingerprint matches ("$0").\n"; else print "\nVerification failed: the fingerprint ("$0") does not match the expected one.\n"}'

4.  添加镜像仓库：

```{=html}
<!-- -->
```
    echo "deb [signed-by=/etc/apt/keyrings/packages.mozilla.org.asc] https://mirrors.ustc.edu.cn/mozilla/apt mozilla main" | sudo tee -a /etc/apt/sources.list.d/mozilla.list > /dev/null

5.  设置优先级，避免 Ubuntu 下 snap 版本被优先安装：

```{=html}
<!-- -->
```
    echo '
    Package: *
    Pin: release a=mozilla
    Pin-Priority: 1000
    ' | sudo tee /etc/apt/preferences.d/mozilla

6.  更新并安装：

```{=html}
<!-- -->
```
    sudo apt-get update && sudo apt-get install firefox
