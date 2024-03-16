#!/usr/bin/python3


"""
4-cities_by_state.py:
script that lists all cities from the database hbtn_0e_4_usa
Usage: ./4-cities_by_state.py <mysql username> <mysql password> <database name>
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

cusrsor = db.cursor()
cusrsor.execute(
    "SELECT c.id, c.name, s.name \
                FROM cities c \
                JOIN  states s \
                ON c.state_id=s.id \
                ORDER BY c.id \
"
)

for row in cusrsor.fetchall():
    print(row)

cusrsor.close()
db.close()
