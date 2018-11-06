#!/usr/bin/env python
# encoding: utf-8

import psycopg2
import socket

# connect database and fetch hosts
try:
    conn = psycopg2.connect(database="testdb", user="postgres", password="PASSWORD", host="DATABASEHOST", port="5432")
    cur = conn.cursor()
    cur.execute("inquire statement")
    rows = cur.fetchall()
    # conn.commit()
except Exception:
    print("Connect database error!")
finally:
    cur.close()
    conn.close()

# use socket module to scan hosts' port to judge blocked servers
blocked_servers = []
for row in rows:
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(3)
    try:
        sk.connect((row[2], 180))
    except Exception:
        blocked_servers.append(row)
    finally:
        sk.close()

# output the blocked servers' information
for blocked_server in blocked_servers:
    with open('./bloeckedServers', 'a') as f:
        f.write("ID: %s, uuid: %s, IP: %s\n" % (blocked_server[0], blocked_server[1], blocked_server[2]))