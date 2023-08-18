#!/usr/bin/python3
"""module lists cities from db hbtn_0e_0_usa"""


if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    try:
        conn = MySQLdb.connect("localhost", username, password, dbname)
        cur = conn.cursor()
        cur.execute("SELECT id, name FROM cities ORDER BY id ASC")
        rows = cur.fetchall()
        for row in rows:
            print("{}".format(row))
    except Exception as e:
        print("Something went wrong... ")
        print(e)
