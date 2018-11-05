#!/usr/bin/python

import socket
import time
#
n = 0
while n < 10:
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(3)
    try:
        sk.connect(('173.255.254.108', 180))
        print("Server port is ok")
    except Exception:
        print("\033[1;31;mServer port 180 is close\033[0m")
    sk.close()
    print(n)
    n += 1
    time.sleep(10)
