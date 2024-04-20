# Hackage

## 地址

<https://mirrors.ustc.edu.cn/hackage/>

## 说明

Hackage 镜像

## Stack 使用说明

编辑 `~/.stack/config.yaml`，增加下列参数

\>= v2.9.3:

    package-index:
      download-prefix: https://mirrors.ustc.edu.cn/hackage/
      hackage-security:
        keyids:
        - 0a5c7ea47cd1b15f01f5f51a33adda7e655bc0f0b0615baa8e271f4c3351e21d
        - 1ea9ba32c526d1cc91ab5e5bd364ec5e9e8cb67179a471872f6e26f0ae773d42
        - 280b10153a522681163658cb49f632cde3f38d768b736ddbc901d99a1a772833
        - 2a96b1889dc221c17296fcc2bb34b908ca9734376f0f361660200935916ef201
        - 2c6c3627bd6c982990239487f1abd02e08a02e6cf16edb105a8012d444d870c3
        - 51f0161b906011b52c6613376b1ae937670da69322113a246a09f807c62f6921
        - 772e9f4c7db33d251d5c6e357199c819e569d130857dc225549b40845ff0890d
        - aa315286e6ad281ad61182235533c41e806e5a787e0b6d1e7eef3f09d137d2e9
        - fe331502606802feac15e514d9b9ea83fee8b6ffef71335479a2e68d84adc6b0
        key-threshold: 3 # number of keys required

        # ignore expiration date, see https://github.com/commercialhaskell/stack/pull/4614
        ignore-expiry: true

\>= v2.1.1, <v2.9.3:

    package-indices:
    - download-prefix: https://mirrors.ustc.edu.cn/hackage/
      hackage-security:
        keyids:
        - 0a5c7ea47cd1b15f01f5f51a33adda7e655bc0f0b0615baa8e271f4c3351e21d
        - 1ea9ba32c526d1cc91ab5e5bd364ec5e9e8cb67179a471872f6e26f0ae773d42
        - 280b10153a522681163658cb49f632cde3f38d768b736ddbc901d99a1a772833
        - 2a96b1889dc221c17296fcc2bb34b908ca9734376f0f361660200935916ef201
        - 2c6c3627bd6c982990239487f1abd02e08a02e6cf16edb105a8012d444d870c3
        - 51f0161b906011b52c6613376b1ae937670da69322113a246a09f807c62f6921
        - 772e9f4c7db33d251d5c6e357199c819e569d130857dc225549b40845ff0890d
        - aa315286e6ad281ad61182235533c41e806e5a787e0b6d1e7eef3f09d137d2e9
        - fe331502606802feac15e514d9b9ea83fee8b6ffef71335479a2e68d84adc6b0
        key-threshold: 3 # number of keys required

        # ignore expiration date, see https://github.com/commercialhaskell/stack/pull/4614
        ignore-expiry: true

< v2.1.1:

    package-indices:
      - name: USTC
        download-prefix: https://mirrors.ustc.edu.cn/hackage/package/
        http: https://mirrors.ustc.edu.cn/hackage/01-index.tar.gz

## Cabal 使用说明

1.  执行 `cabal user-config init`
2.  修改 `~/.cabal/config`

    - Cabal ≥ 1.24 (GHC 8.0)

        找到官方仓库：

            repository hackage.haskell.org
              url: http://hackage.haskell.org/
              -- secure: True
              -- root-keys:
              -- keys-threshold: 3

        改为科大源：

            repository mirrors.ustc.edu.cn
              url: https://mirrors.ustc.edu.cn/hackage/
              secure: True

        !!! note

            首次 `cabal update` 时会提示
            `Warning: No mirrors found for http://mirrors.ustc.edu.cn/hackage/`，
            该警告可忽略。

        !!! warning

            为了保证与老版本 cabal 的兼容性， `secure` 值设置为 `False` 可能导致
            cabal 无法获取到最新的包信息。

    - Cabal < 1.24

        找到官方仓库: :

            remote-repo: hackage.haskell.org:http://hackage.haskell.org/packages/archive

        改为科大源: :

            remote-repo: mirrors.ustc.edu.cn:http://mirrors.ustc.edu.cn/hackage/

3.  执行 `cabal update`

## 相关链接

官方主页

:   <https://hackage.haskell.org/>

Cabal

:   <https://www.haskell.org/cabal/>

Stack

:   <https://docs.haskellstack.org/en/stable/README/>
