# debuginfod 缓存

debuginfod 是通过 HTTP API 按二进制程序的 build ID 提供调试信息、可执行文件和源代码的服务，GDB 等工具可以通过它自动获取调试所需的文件。build ID 类似于程序的身份信息，可以独一无二区分不同的编译参数编译的程序。程序的 build ID 可以使用 `file` 查看：

```console
$ file /usr/bin/ls
/usr/bin/ls: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=d6281af586ce362d9c1029002636397df0cf21f1, for GNU/Linux 4.4.0, stripped
```

本镜像站目前提供 Ubuntu、Debian 和 Arch Linux 的 debuginfod **缓存**。

!!! warning "测试中"
    本镜像处于测试阶段，以下内容可能发生变化。

## 同步细节

调试信息（`debuginfo`）和可执行文件（`executable`）根据用户访问情况，每天更新一次缓存。**在请求未命中时，会 302 重定向到对应发行版的源站点**。本镜像不是完整镜像，因此仍然需要用户到源站点有基本的可连通性。

源代码（`source`）和单独的 ELF/DWARF 节（`section`）等其他请求直接重定向到源站点。

## 配置方法

根据所需调试信息所属的发行版，在终端中设置 `DEBUGINFOD_URLS` 环境变量，然后从该终端启动 GDB 等工具：

=== "Ubuntu"

    ```shell
    export DEBUGINFOD_URLS="https://mirrors.ustc.edu.cn/debuginfod/ubuntu/"
    ```

=== "Debian"

    ```shell
    export DEBUGINFOD_URLS="https://mirrors.ustc.edu.cn/debuginfod/debian/"
    ```

=== "Arch Linux"

    ```shell
    export DEBUGINFOD_URLS="https://mirrors.ustc.edu.cn/debuginfod/archlinux/"
    ```

如需持久生效，可将对应命令添加到所用 shell 的启动文件中，例如 Bash 的 `~/.bashrc`。

删除上述环境变量设置即可恢复发行版默认的 debuginfod 配置。作为参考，以下是各个发行版的 debuginfod 服务器地址：

| 发行版 | 上游地址 |
| --- | --- |
| Ubuntu | `https://debuginfod.ubuntu.com/` |
| Debian | `https://debuginfod.debian.net/` |
| Arch Linux | `https://debuginfod.archlinux.org/` |

## 调试方法

安装提供 `debuginfod-find` 的软件包后，可以在设置上述环境变量的终端中测试下载：

```shell
DEBUGINFOD_VERBOSE=1 DEBUGINFOD_CACHE_PATH="$(mktemp -d)" \
    debuginfod-find debuginfo /usr/bin/true
```

该命令使用临时缓存目录，避免命中已有本地缓存；详细输出中可以看到请求地址和 HTTP 响应状态。

上游不一定提供所有版本、所有程序的调试信息。若输出中出现 HTTP 404 和 `Server query failed: No such file or directory`，表示请求的 build ID 对应的调试信息不可用，可换用其他程序测试。

## 相关链接

elfutils debuginfod

:   <https://sourceware.org/elfutils/Debuginfod.html>

GDB debuginfod 配置

:   <https://sourceware.org/gdb/current/onlinedocs/gdb.html/Debuginfod-Settings.html>
