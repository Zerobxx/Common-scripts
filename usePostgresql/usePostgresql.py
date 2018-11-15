#!/usr/bin/env python
# encoding: utf-8

import psycopg2

# connect database and fetch hosts info
try:
    conn = psycopg2.connect(database="testdb", user="postgres", password="PASSWORD", host="DATABASEHOST", port="5432")
    cur = conn.cursor()
    cur.execute("inquire statement")
    rows = cur.fetchall()
    conn.commit()
except Exception:
    print("Connect database error!")
finally:
    cur.close()
    conn.close()

for row in rows:
    print(row[2])
