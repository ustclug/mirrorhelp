# Kubernetes

## 地址

<https://mirrors.ustc.edu.cn/kubernetes>

## 说明

Kubernetes APT/YUM 软件源，从 OpenSUSE OBS 构建同步。

## 收录版本

稳定版（`stable:`）

## 使用说明

### APT

1. 在配置中添加镜像（注意修改为自己需要的版本号）：

    ```shell
    echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://mirrors.ustc.edu.cn/kubernetes/core:/stable:/v1.28/deb/ /" | sudo tee /etc/apt/sources.list.d/kubernetes.list
    ```

2. 添加公钥（所有仓库均使用相同公钥，因此 URL 中版本号可以忽略）：

    ```shell
    curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.28/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
    ```

3. 更新软件源：

    ```shell
    sudo apt-get update
    ```

### YUM

执行如下命令（注意修改为自己需要的版本号）：

```shell
cat <<EOF | sudo tee /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://mirrors.ustc.edu.cn/kubernetes/core:/stable:/v1.28/rpm/
enabled=1
gpgcheck=1
gpgkey=https://pkgs.k8s.io/core:/stable:/v1.28/rpm/repodata/repomd.xml.key
exclude=kubelet kubeadm kubectl cri-tools kubernetes-cni
EOF
```

## 相关链接

pkgs.k8s.io: Introducing Kubernetes Community-Owned Package Repositories

:   <https://kubernetes.io/blog/2023/08/15/pkgs-k8s-io-introduction/>

Kubernetes Legacy Package Repositories Will Be Frozen On September 13, 2023

:   <https://kubernetes.io/blog/2023/08/31/legacy-package-repository-deprecation/>
