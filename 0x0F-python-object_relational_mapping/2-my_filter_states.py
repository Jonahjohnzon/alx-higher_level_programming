#!/usr/bin/python3
"""  lists all states from  database """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    curso = db.cursor()
    curso.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
    rowz = curso.fetchall()
    for a in rowz:
        print(a)
    curso.close()
    db.close()
