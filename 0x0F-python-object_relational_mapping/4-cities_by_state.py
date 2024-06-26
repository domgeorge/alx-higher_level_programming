#!/usr/bin/python3
"""Lists all of the cities from the database hbtn_0e_4_usa"""


import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])

    cur = conn.cursor()
    query = ("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    cur.execute(query)
    rows = cur.fetchall()

    for res in rows:
        print(res)

    cur.close()
    conn.close()
