#!/usr/bin/python3

"""
3-my_safe_filter_states.py:
script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
Usage: ./3-my_safe_filter_states.py <mysql username> <mysql password>
<database name> <state name searched>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
    cursor = db.cursor()
    name = sys.argv[4]
    cursor.execute("SELECT * FROM states WHERE name = %s", (name,))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
