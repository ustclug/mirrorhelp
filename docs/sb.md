# n.wtf

## 地址

<https://mirrors.ustc.edu.cn/sb/nginx>

## 说明

n.wtf 是对 Nginx 最新主线版本的第三方 Debian 包，支持诸如 TLS 1.3、Brotil/Zstd 压缩、QUIC、HTTP/3 等功能。

## 使用说明

安装必要的前置依赖，以及公钥：

```sh
sudo apt install -y lsb-release ca-certificates curl gnupg dpkg

curl -sSL https://n.wtf/public.key | sudo bash -c 'gpg --dearmor > /usr/share/keyrings/n.wtf.gpg'
```

之后添加软件源：

=== "`sources.list` 格式"

    ```sh
    sudo bash -c 'echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/n.wtf.gpg] https://mirrors.ustc.edu.cn/sb/nginx/ $(lsb_release -sc) main" > /etc/apt/sources.list.d/n.wtf.list'
    ```

=== "DEB822 格式"

    ```sh
    sudo bash -c 'cat > /etc/apt/sources.list.d/n.wtf.sources << EOF
    Components: main
    Architectures: $(dpkg --print-architecture)
    Suites: $(lsb_release -cs)
    Types: deb
    URIs: https://mirrors.ustc.edu.cn/sb/nginx/
    Signed-By: /usr/share/keyrings/n.wtf.gpg
    EOF'
    ```

## 相关链接

官方主页

:   <https://n.wtf/>
