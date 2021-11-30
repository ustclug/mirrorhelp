========================
Raspbian Addons 源使用帮助
========================

地址
====

https://mirrors.ustc.edu.cn/raspbian-addons/

说明
====

Raspbian Addons 是 Raspbian 非官方软件源，含有许多来自 GitHub 的开源软件，可作为对 Raspbian（Debian） 官方仓库的一个补充。

使用说明
========

信任仓库的 GPG 公钥::

  wget -qO- https://mirrors.ustc.edu.cn/raspbian-addons/KEY.gpg | sudo apt-key add -


添加该仓库::

  echo "deb https://mirrors.ustc.edu.cn/raspbian-addons/debian/ /" | sudo tee /etc/apt/sources.list.d/rpirepo.list

更新软件包缓存::

  sudo apt update

相关链接
========

:项目主页: https://raspbian-addons.org
:官方文档: https://docs.raspbian-addons.org
:GitHub 主页: https://github.com/raspbian-addons
