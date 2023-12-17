#!/usr/bin/python3
import MySQLdb
import sys
"""  lists all states"""


if __name__ == "__main__":
    datab = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    curs = datab.cursor()
    curs.execute("SELECT * FROM states")
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    datab.close()
