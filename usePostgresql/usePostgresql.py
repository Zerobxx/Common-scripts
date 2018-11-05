#!/usr/bin/python
#

import psycopg2

conn = psycopg2.connect(database="testdb", user="postgres", password="PASSWORD", host="DATABASEHOST", port="5432")
cur = conn.cursor()
cur.execute("inquire statement")

rows = cur.fetchall()

for row in rows:
    print("uuid=" + row[1] + ", " + "host=" + row[2])

conn.close()
