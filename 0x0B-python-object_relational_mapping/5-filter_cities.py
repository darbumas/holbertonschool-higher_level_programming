#!/usr/bin/python3
"""Script takes 'state' as argv[4] & lists all cities of that state
from db 'hbtn_0e_4_usa'"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states ON" +
                " cities.state_id = states.id WHERE states.name = %s",
                (argv[4], ))
    print(", ".join(row[0] for row in cur.fetchall()))
    cur.close()
    db.close()
