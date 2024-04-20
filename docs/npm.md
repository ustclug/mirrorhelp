# NPM 反向代理

中科大镜像站的 npm 镜像是 <https://registry.npmjs.org/> 的反代。

## 使用说明

编辑 `~/.npmrc` ，添加

    registry=https://npmreg.proxy.ustclug.org/

若不想将本源设置为默认源，只想使用本源安装某个软件包，可在安装包时采用以下用法：

    npm --registry https://npmreg.proxy.ustclug.org/ install <packagename>

## 注意事项

不支持 publish，若出现错误，请将 `~/.npmrc`
中的用户名密码部分注释掉，并删除缓存 (`rm -rf ~/.npm`)
重试。

## 相关链接

官方主页

:   <https://www.npmjs.org/>
