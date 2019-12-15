#!/usr/bin/python3
import sys
import MySQLdb
"""
This script connect to a database and print te obj
"""
if __name__ == "__main__":
    # Get the data
    user = sys.argv[1]
    pas = sys.argv[2]
    db = sys.argv[3]

    # Create the connection
    db = MySQLdb.connect(host='localhost',
                         user=user,
                         passwd=pas,
                         db=db)

    # Get the cursor, this is to create difrents
    # working env
    cur = db.cursor()
    # Select cities
    cur.execute("SELECT cities.id, cities.name, states.name "
                "FROM cities JOIN states "
                "ON cities.state_id = states.id "
                "ORDER BY cities.id")

    # Get the rdata of the query and print
    rows = cur.fetchall()
    for row in rows:
        print(row)
