# CPAN

## 地址

<https://mirrors.ustc.edu.cn/CPAN/>

## 使用说明

若你以前从未使用过 CPAN，请在命令行下运行 cpan

    Would you like me to automatically choose some CPAN mirror sites for you? (This means connecting to the Internet) [yes]

此处输入 no

    Would you like to pick from the CPAN mirror list? [yes]

此处直接回车

    You should select more than one (just in case the first isn't available).

    (1) Africa
    (2) Asia
    (3) Europe
    (4) North America
    (5) Oceania
    (6) South America
    Select your continent (or several nearby continents) []

此处选择 2

    (1) China
    (2) India
    (3) Indonesia
    (4) Israel
    (5) Japan
    (6) Kazakhstan
    (7) Pakistan
    (8) Republic of Korea
    (9) Saudi Arabia
    (10) Singapore
    (11) Taiwan
    (12) Thailand
    (13) Turkey
    (14) Viet Nam
    Select your country (or several nearby countries) []

此处选择 1，然后选择科大源即可。

若你已经用过 cpan 了，将 `~/.cpan/CPAN/MyConfig.pm` 中的 `'urllist'` 的值改为：

    'urllist' => [q[http://mirrors.ustc.edu.cn/CPAN/]],

## 相关链接

- 官方主页：<http://www.cpan.org/>
- 镜像列表：<http://www.cpan.org/SITES.html>
- FAQ: <http://www.cpan.org/misc/cpan-faq.html>
