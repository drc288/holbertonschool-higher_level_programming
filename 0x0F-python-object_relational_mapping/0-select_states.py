#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    user = sys.argv[1]
    pas = sys.argv[2]
    db = sys.argv[3]

    db = MySQLdb.connect(host='localhost',
                         user=user,
                         passwd=pas,
                         db=db)

    cur = db.cursor()
    cur.execute("SELECT * FROM states")

    rows = cur.fetchall()
    for row in rows:
        print(row)

