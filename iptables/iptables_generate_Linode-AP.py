#!/usr/bin/env python
# encoding: utf-8

a_list = []

with open('./Linode-AP', 'r') as f:
    for CIDR in f.readlines():
        a_addr = CIDR.split('.')[0]
        if a_addr not in a_list:
            a_list.append(a_addr)

with open('./iptables_Linode-AP.sh', 'a') as f:
    for a in a_list:
        f.write('iptables -A INPUT -s %s.0.0.0/8 -j ACCEPT\n' % a)


