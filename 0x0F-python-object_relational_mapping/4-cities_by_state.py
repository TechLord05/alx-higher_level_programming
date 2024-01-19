#!/usr/bin/python3
"""
    This module lists all cities safely from the database
    hbtn_0e_0_usa.
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

    # Create a cursor object
    cursor = db.cursor()

    cursor.execute("""SELECT cities.id, cities.name, states.name FROM
                   cities JOIN states ON cities.state_id = states.id
                   ORDER BY cities.id""")

    output = cursor.fetchall()

    for r in output:
        print(r)

    cursor.close()
    db.close()
