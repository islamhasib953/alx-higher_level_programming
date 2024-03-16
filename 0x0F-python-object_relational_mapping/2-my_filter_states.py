#!/usr/bin/python3

"""
2-my_filter_states.py:
script that takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
Usage: ./2-my_filter_states.py
<mysql username> <mysql password> <database name> <search name>
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
        charset="utf8",
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states` WHERE `name`='{}'".format(sys.argv[4]))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
