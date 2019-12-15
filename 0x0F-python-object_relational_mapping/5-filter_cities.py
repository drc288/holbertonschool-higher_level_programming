#!/usr/bin/python3
import sys
import MySQLdb
"""
This script connect to a database and print te obj
where state_n is the value to serch in cities
"""
if __name__ == "__main__":
    # Get the data
    user = sys.argv[1]
    pas = sys.argv[2]
    db = sys.argv[3]
    state_n = sys.argv[4]
    i = 0

    # Create the connection
    db = MySQLdb.connect(host='localhost',
                         user=user,
                         passwd=pas,
                         db=db)

    # Get the cursor, this is to create difrents
    # working env
    cur = db.cursor()
    # Create the consult
    cur.execute("SELECT cities.name "
                "FROM cities JOIN states "
                "ON cities.state_id = states.id "
                "WHERE states.name LIKE BINARY  %(state_n)s"
                "ORDER BY cities.id", {'state_n': state_n})

    # Get the data of the query and print
    rows = cur.fetchall()
    rows_l = len(rows) - 1
    for row in rows:
        if i != rows_l:
            i += 1
            print(row[0], end=", ")
        else:
            print(row[0])
