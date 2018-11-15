#### net.sh

使用方法（如指定计算网卡eth0）：

```shell
# bash net.sh NIC
# 如指定网卡eth0
bash net.sh eth0
```



通过计算每隔一秒钟 /proc/net/dev 收发正确包数的差值来计算指定网卡的实时流量。

注：/proc/net/dev 记录从开机以来网卡的流量总值，不断累积，重启清零，许多网络命令显示实时流量都是通过对此计算而来



