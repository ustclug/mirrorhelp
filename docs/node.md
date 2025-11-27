# Node

## 地址

<https://mirrors.ustc.edu.cn/node/>

## 说明

Node.js 仓库镜像，包含了 <https://nodejs.org/dist/> 中的内容

## nvm 更改 Node.js 镜像为科大源

设置环境变量 `NVM_NODEJS_ORG_MIRROR` 为 `https://mirrors.ustc.edu.cn/node/` 即可。

## n 更改 Node.js 镜像为科大源

设置环境变量 `NODE_MIRROR` 为 `https://mirrors.ustc.edu.cn/node/` 即可。

## fnm 更改 Node.js 镜像为科大源

设置环境变量 `FNM_NODE_DIST_MIRROR` 为 `https://mirrors.ustc.edu.cn/node/` 即可。

## volta 更改 Node.js 镜像为科大源

创建或编辑 ~/.volta/hooks.json (Linux/MacOS)，或 %LOCALAPPDATA%\Volta\hooks.json (Windows)，将内容替换如下
```json
{
    "node": {
        "index": {
            "template": "https://mirrors.ustc.edu.cn/node/index.json"
        },
        "distro": {
            "template": "https://mirrors.ustc.edu.cn/node/v{{version}}/{{filename}}"
        }
    }
}
```

## 相关链接

Node.js 官网

:   <https://nodejs.org/>

nvm

:   <https://github.com/nvm-sh/nvm>

n

:   <https://github.com/tj/n>

fnm

:   <https://github.com/Schniz/fnm>
