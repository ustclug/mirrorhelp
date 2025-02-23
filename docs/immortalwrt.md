# ImmortalWrt

## 地址

<https://mirrors.ustc.edu.cn/immortalwrt/>

## 说明

ImmortalWrt 是 OpenWrt 的一个第三方分支，主要针对国人用户开发，提供更多的本地化软件包和设备支持。

## 使用说明

SSH 登录路由器编辑 `/etc/opkg/distfeeds.conf` 文件，将源地址 `https://downloads.immortalwrt.org` 或 `https://mirrors.vsean.net/openwrt` 更改为 `https://mirrors.ustc.edu.cn/immortalwrt`。

可以使用如下命令操作：

```shell
sed -e 's|https://downloads.immortalwrt.org|https://mirrors.ustc.edu.cn/immortalwrt|g' \
    -e 's|https://mirrors.vsean.net/openwrt|https://mirrors.ustc.edu.cn/immortalwrt|g' \
    -i.old /etc/opkg/distfeeds.conf
```

之后运行 `opkg update` 更新软件索引，注意检查是否出现错误。

!!! tip

    如果你使用的 ImmortalWrt 版本 >= 23.05.0，也可以使用如下命令设置镜像：

    ```shell
    uci set system.@imm_init[0].opkg_mirror='https://mirrors.ustc.edu.cn/immortalwrt'
    uci commit system
    ```

## 相关链接

官方主页

:   <https://github.com/immortalwrt>

软件源仓库

:   <https://github.com/immortalwrt/packages>
