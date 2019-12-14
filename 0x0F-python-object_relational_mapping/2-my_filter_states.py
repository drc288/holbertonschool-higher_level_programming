#!/usr/bin/python3
import sys
import MySQLdb
"""
This script print the data with the state_n
"""
if __name__ == "__main__":
    if len(sys.argv) == 5:
        user = sys.argv[1]
        pas = sys.argv[2]
        db = sys.argv[3]
        state_n = sys.argv[4]

        db = MySQLdb.connect(host='localhost',
                             user=user,
                             passwd=pas,
                             db=db)

        cur = db.cursor()
        cur.execute("SELECT * FROM states "
                    "WHERE name=\'{:s}\' "
                    "ORDER BY states.id ASC".format(state_n))
        rows = cur.fetchall()

        for row in rows:
            print(row)
