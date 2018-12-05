#!/bin/bash

iptables -A INPUT -s 45.33.0.0/16 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 45.56.0.0/16 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 45.79.0.0/16 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 45.118.132.0/22 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 23.0.0.0/8 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 50.116.0.0/16 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 66.0.0.0/8 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 64.0.0.0/9 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 96.126.0.0/16 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 69.0.0.0/9 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 69.164.0.0/8 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 65.0.0.0/10 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 70.0.0.0/9 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 74.0.0.0/8 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 85.0.0.0/8 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 104.192.0.0/10 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 213.0.0.0/8 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 75.127.0.0/16 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 88.80.184.0/21 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 97.107.128.0/20 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 198.0.0.0/9 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 212.0.0.0/9 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 173.192.0.0/10 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 109.0.0.0/8 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 103.3.60.0/22 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 103.29.68.0/22 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 67.18.0.0/16 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 139.162.0.0/16 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 172.104.0.0/16 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 209.123.0.0/16 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 207.192.0.0/16 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 192.81.0.0/16 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 192.155.0.0/16 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 72.14.176.0/20 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 178.79.128.0/18 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 176.58.96.0/19 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 151.236.216.0/21 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 162.216.16.0/22 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 80.85.84.0/22 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -s 185.3.92.0/22 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A INPUT -s 127.0.0.1 -j ACCEPT
iptables -A INPUT -s 0.0.0.0/0 -j DROP