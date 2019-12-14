#!/usr/bin/python3
import sys
import MySQLdb
"""
This script get all data where init wiht n
"""
if __name__ == "__main__":
    if len(sys.argv) == 4:
        # Get the data
        user = sys.argv[1]
        pas = sys.argv[2]
        db = sys.argv[3]

        # Create the conection
        db = MySQLdb.connect(host='localhost',
                             user=user,
                             passwd=pas,
                             db=db)

        # Get new instance
        cur = db.cursor()
        # Execute the query
        # PSDT: LIKE using and search the data with init n or N
        cur.execute("SELECT * FROM states WHERE name LIKE 'n%' ORDER BY states.id ASC")
        rows = cur.fetchall()
        # Print the data
        for row in rows:
            print(row)
