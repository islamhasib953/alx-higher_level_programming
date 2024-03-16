#!/usr/bin/python3

"""
0-select_states.py:
script that lists all states from the database hbtn_0e_0_usa
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
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

    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


# import MySQLdb

# # Connect to the MySQL database
# conn = MySQLdb.connect(
#     host="localhost",  # Your host
#     user="root",   # Your username
#     passwd="root", # Your password
#     db="islam" # Your database name
# )

# # Create a cursor object to execute queries
# cursor = conn.cursor()

# # Example query: select all rows from a table
# query = "SELECT * FROM student"

# # Execute the query
# cursor.execute(query)

# # Fetch all rows from the result set
# rows = cursor.fetchall()

# # Print each row
# for row in rows:
#     print(row)

# # Close cursor and connection
# cursor.close()
# conn.close()
