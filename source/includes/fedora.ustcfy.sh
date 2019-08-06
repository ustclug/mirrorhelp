#!/bin/sh
set -e
for f in fedora-modular.repo fedora-updates-modular.repo fedora-updates.repo fedora.repo;do
  cp "/etc/yum.repos.d/$f" "/etc/yum.repos.d/$f~"
  sed -i 's|^#baseurl=http://download.fedoraproject.org/pub/fedora/linux|baseurl=https://mirrors.ustc.edu.cn/fedora|g' "/etc/yum.repos.d/$f"
  sed -i 's|^metalink=|#metalink=|g' "/etc/yum.repos.d/$f"
done
