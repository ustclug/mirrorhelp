# Stackage

## 地址

<https://mirrors.ustc.edu.cn/stackage/>

## 说明

Stackage 镜像

## 使用说明

推荐搭配 USTC Hackage 源使用：[hackage](hackage.md)

编辑 `~/.stack/config.yaml`, 根据版本的不同，增加下列配置：

=== ">= 3.1.1"

    ```yaml
    setup-info-locations:
      - http://mirrors.ustc.edu.cn/stackage/stack-setup.yaml
    urls:
      latest-snapshot: http://mirrors.ustc.edu.cn/stackage/snapshots.json
    snapshot-location-base: http://mirrors.ustc.edu.cn/stackage/stackage-snapshots/
    global-hints-location:
      url: https://mirrors.ustc.edu.cn/stackage/stackage-content/stack/global-hints.yaml
    ```

=== ">= 2.5, < 3.1.1"

    ```yaml
    setup-info-locations:
      - http://mirrors.ustc.edu.cn/stackage/stack-setup.yaml
    urls:
      latest-snapshot: http://mirrors.ustc.edu.cn/stackage/snapshots.json
    snapshot-location-base: http://mirrors.ustc.edu.cn/stackage/stackage-snapshots/
    ```

=== ">= 2.3, < 2.5"

    ```yaml
    setup-info-locations:
      - http://mirrors.ustc.edu.cn/stackage/stack-setup.yaml
    urls:
      latest-snapshot: http://mirrors.ustc.edu.cn/stackage/snapshots.json
    ```

=== ">= v2.1.1, < 2.3"

    ```yaml
    setup-info: "http://mirrors.ustc.edu.cn/stackage/stack-setup.yaml"
    urls:
      latest-snapshot: http://mirrors.ustc.edu.cn/stackage/snapshots.json
    ```

=== "< v2.1.1"

    ```yaml
    setup-info: "http://mirrors.ustc.edu.cn/stackage/stack-setup.yaml"
    urls:
      latest-snapshot: http://mirrors.ustc.edu.cn/stackage/snapshots.json
      lts-build-plans: http://mirrors.ustc.edu.cn/stackage/lts-haskell/
      nightly-build-plans: http://mirrors.ustc.edu.cn/stackage/stackage-nightly/
    ```

此外，如果版本低于 3.1.1，还需要手动下载 <https://mirrors.ustc.edu.cn/stackage/stackage-content/stack/global-hints.yaml> 到 `~/.stack/pantry/global-hints-cache.yaml`（在 Windows 下是 `%APPDATA%\stack\pantry\global-hints-cache.yaml`）。注意文件名不同。这是由于旧版本 stack 暂时不支持配置该文件的上游地址。该文件需要在每当第一次用到新版本的 GHC 时更新。

## 相关链接

官方主页

:   <https://www.stackage.org/>

Stack

:   <https://docs.haskellstack.org/en/stable/README/>
