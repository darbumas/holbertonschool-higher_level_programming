#!/usr/bin/python3
""" Script lists all states with names starting with 'N' from db hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
