# Ubuntu 各分区挂载说明
- 256G SSD + 3T 机械

- /boot    引导分区
    - 1024MB
- SWAP     交换空间
    - 内存容量 X 2
- /home    主目录
    - 102400MB
- /        根目录
    - 未指定挂载点的目录都在这里
- /tmp     临时文件目录
    - 5120MB
- /usr     文件系统, 安装的软件程序在这里
    - 20480MB
- /var     可变数据目录
    - 5120MB
- /srv     系统服务目录
    - 10240MB
- /opt     附加应用程序
    - 机械
- /usr/local