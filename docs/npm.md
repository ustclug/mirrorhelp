# NPM 反向代理

中科大镜像站的 npm 镜像是 <https://registry.npmjs.org/> 的反代。

!!! warning

    由于服务压力过高且存在更好的 NPM 镜像（如阿里云的 [npmmirror 镜像站](https://npmmirror.com/)），本反向代理服务已于 2026-06-12 停止服务，所有请求将被 302 至 npmmirror。

## 注意事项

不支持 publish，若出现错误，请将 `~/.npmrc` 中的用户名密码部分注释掉，并删除缓存（`rm -rf ~/.npm`）重试。

## 相关链接

官方主页

:   <https://www.npmjs.org/>
