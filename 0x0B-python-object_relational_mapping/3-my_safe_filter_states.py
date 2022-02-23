#!/usr/bin/python3
"""Script matches argv[4] to all values in table 'states' from db
'hbtn_0e_0_usa' safe from MySQL injections"""
from sys import argv
import MySQLdb


if __name__ == "__main__":

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id",
                (argv[4], ))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
