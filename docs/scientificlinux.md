# Scientific Linux

## 收录版本

6, 7

## 使用说明

以 6.x 为例，下载 sl-ustc.repo 放入 `/etc/yum.repo.d/` 中。

```ini title="sl-ustc.repo"
[sl]
name=Scientific Linux $releasever - $basearch - ustc.edu.cn
baseurl=http://mirrors.ustc.edu.cn/scientificlinux/$releasever/$basearch/os/
#mirrorlist=http://ftp.scientificlinux.org/linux/scientific/mirrorlist/sl-base-6.txt
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-sl file:///etc/pki/rpm-gpg/RPM-GPG-KEY-sl6 file:///etc/pki/rpm-gpg/RPM-GPG-KEY-cern

[sl-security]
name=Scientific Linux $releasever - $basearch - security updates - ustc.edu.cn
baseurl=http://mirrors.ustc.edu.cn/scientificlinux/$releasever/$basearch/updates/security/
#mirrorlist=http://ftp.scientificlinux.org/linux/scientific/mirrorlist/sl-security-6.txt
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-sl file:///etc/pki/rpm-gpg/RPM-GPG-KEY-sl6 file:///etc/pki/rpm-gpg/RPM-GPG-KEY-cern


[sl-source]
name=Scientific Linux $releasever - Source - ustc.edu.cn
baseurl=http://mirrors.ustc.edu.cn/scientificlinux/$releasever/SRPMS/
enabled=0
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-sl file:///etc/pki/rpm-gpg/RPM-GPG-KEY-sl6 file:///etc/pki/rpm-gpg/RPM-GPG-KEY-cern
```

运行 `yum makecache` 生成缓存。
