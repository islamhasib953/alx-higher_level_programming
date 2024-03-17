#!/usr/bin/python3

"""
5-filter_cities.py:
script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
Usage: ./5-filter_cities.py <mysql username>
<mysql password> <database name>
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
    name = sys.argv[4]
    cusrsor.execute(
        """
    SELECT c.name
                    FROM cities c
                    JOIN  states s
                    ON c.state_id=s.id
                    WHERE s.name = %s
                ORDER BY c.id
    """,
        (name,),
    )

    for row in cusrsor.fetchall():
        print(row)

    cusrsor.close()
    db.close()
