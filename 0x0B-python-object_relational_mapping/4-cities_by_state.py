#!/usr/bin/python3
"""Script lists all cities from db 'hbtn_0e_0_usa'"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities" +
                " JOIN states ON cities.state_id = states.id")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
