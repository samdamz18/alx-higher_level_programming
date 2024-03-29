#!/usr/bin/python3
"""A python script that takes in the name of a state as an argument and lists
all cities of that state, using the database `hbtn_0e_4_usa`
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])

    cur = conn.cursor()
    cur.execute(
        "SELECT cities.id, cities.name FROM cities JOIN states \
        ON cities.state_id = states.id \
        WHERE states.name LIKE BINARY %(state_name)s \
        ORDER BY cities.id ASC", {'state_name': argv[4]}
    )

    rows = cur.fetchall()

    # pretty print values
    rows_len = len(rows)
    for i in range(rows_len):
        print(rows[i][1], end='')
        print('' if i == rows_len - 1 else ', ', end='')
    print()
