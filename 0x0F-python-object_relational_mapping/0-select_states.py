#!/usr/bin/python3
"""module lists states from db hbtn_0e_0_usa"""

import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
dbname = sys.argv[3]

print ("name: {}, passwod: {}, db: {}".format(username, password, dbname))

try:
    conn= MySQLdb.connect("127.0.0.1", username, password, dbname)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print ("{}".format(row))
except Exception as e:
  print("Something went wrong... ")
  print(e)