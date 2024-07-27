# NVIDIA Container 运行时库

## 地址

<https://mirrors.ustc.edu.cn/libnvidia-container/>

## 说明

以 Apache-2.0 协议开源的 NVIDIA Container Toolkit 的二进制软件包

## 使用说明

以下说明修改自 [Installing the NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)。

### Apt

```sh
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://mirrors.ustc.edu.cn/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://nvidia.github.io#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://mirrors.ustc.edu.cn#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

然后安装：

```sh
sudo apt update && sudo apt install nvidia-container-toolkit
```

### Yum / Dnf

```sh
curl -s -L https://mirrors.ustc.edu.cn/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo | \
  sed 's#nvidia.github.io/libnvidia-container/stable/#mirrors.ustc.edu.cn/libnvidia-container/stable/#g' |
  sed 's#nvidia.github.io/libnvidia-container/experimental/#mirrors.ustc.edu.cn/libnvidia-container/experimental/#g' |
  sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo
```

然后安装：

```sh
sudo yum install nvidia-container-toolkit
```

## 相关链接

上游仓库

:   <https://github.com/NVIDIA/libnvidia-container/>
