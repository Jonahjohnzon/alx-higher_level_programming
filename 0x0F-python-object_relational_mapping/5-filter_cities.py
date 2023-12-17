#!/usr/bin/python3
"""  lists all states from database """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    curso = db.cursor()
    curso.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    row = curso.fetchall()
    tmps = list(x[0] for x in row)
    print(*tmps, sep=", ")
    curso.close()
    db.close()
