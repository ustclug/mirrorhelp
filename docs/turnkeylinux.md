# TurnKey Linux

## 地址

<https://mirrors.ustc.edu.cn/turnkeylinux/>

## 说明

TurnKey Linux 提供了一系列预装和预配置的虚拟机镜像（"appliances"），包含了不同用途的服务器软件。

## 使用说明

### 下载 appliance

可在 <https://mirrors.ustc.edu.cn/turnkeylinux/images/> 浏览并下载需要的 appliance 文件。

### 配置 appliance 中的 APT

在 appliance 中将 `/etc/apt/sources.list.d` 下所有文件中 `archive.turnkeylinux.org` 替换为 `mirrors.ustc.edu.cn/turnkeylinux/apt`。

### 配置 Proxmox VE 下载 TurnKey Linux 容器镜像

首先，将 `/usr/share/perl5/PVE/APLInfo.pm` 文件中默认的源地址 `https://releases.turnkeylinux.org/pve` 替换为 `https://mirrors.ustc.edu.cn/turnkeylinux/metadata/pve`：

```sh
sed -i.bak 's|https://releases.turnkeylinux.org|https://mirrors.ustc.edu.cn/turnkeylinux/metadata|g' /usr/share/perl5/PVE/APLInfo.pm
```

然后执行 `systemctl restart pvedaemon` 重新加载配置。

!!! note

    `/usr/share/perl5/PVE/APLInfo.pm` 文件属于 pve-manager 软件包，该软件包升级后，需要重新替换 URL。

然而，TurnKey Linux 提供的 `aplinfo.dat` 中的 URL 不是相对路径，因此还需要修改其内容。参考 [TurnKey Linux 开发者的建议](https://github.com/turnkeylinux/tracker/issues/1963)，修改 `pve-daily-update.service` 的配置：

```sh
mkdir -p /etc/systemd/system/pve-daily-update.service.d/
cat > /etc/systemd/system/pve-daily-update.service.d/update-turnkey-releases.conf <<EOF
[Service]
ExecStopPost=/bin/sed -i 's|http://mirror.turnkeylinux.org|https://mirrors.ustc.edu.cn|' /var/lib/pve-manager/apl-info/releases.turnkeylinux.org
EOF
```

重新加载 systemd 服务并测试：

```sh
systemctl daemon-reload
systemctl start pve-daily-update.service
```

最后确认修改成功完成：

```console
$ grep -c http://mirror.turnkeylinux.org /var/lib/pve-manager/apl-info/releases.turnkeylinux.org
0
$ grep -c https://mirrors.ustc.edu.cn /var/lib/pve-manager/apl-info/releases.turnkeylinux.org
110
```

## 相关链接

官方网站

:   <https://www.turnkeylinux.org/>
