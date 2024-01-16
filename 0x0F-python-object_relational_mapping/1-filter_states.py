#!/usr/bin/python3

"""
Script that lists all states from the database hbtn_0e_0_usa.
Parameters for script: mysql username, mysql password, database name.
Must use the `MySQLdb` module.
Script should connect to a MySQL server runnimg on `localhost` at port `3306`
Results must be in ascending order by `states.id`.
Code should not be executed when imported.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Establish a secure connection to MySQLdb
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    # Creating a cursor object to execute SQL queries
    cursor = db.cursor()

    # Executing the cursor to retrieve states starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch the result
    rows = cursor.fetchall()

    # Loop through the Rows variable to output result
    for row in rows:
        if row[1][0] == 'N':
            print(row)

    # Close the cursor and db connection
    cursor.close()
    db.close()
