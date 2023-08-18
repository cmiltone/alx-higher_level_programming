#!/usr/bin/python3
"""module lists cities from db hbtn_0e_0_usa"""


if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    name = sys.argv[4]

    try:
        conn = MySQLdb.connect("localhost", username, password, dbname)
        cur = conn.cursor()
        cur.execute("""
                SELECT
                    cities.name
                FROM
                    cities
                INNER JOIN states ON cities.state_id=states.id
                WHERE
                    states.name LIKE %(name)s
             """, {
                 'name': name
                })
        rows = cur.fetchall()
        rs = []
        for row in rows:
            rs.append(row[0])
        rs = ", ".join(rs)
        print(rs)
    except Exception as e:
        print("Something went wrong... ")
        print(e)
