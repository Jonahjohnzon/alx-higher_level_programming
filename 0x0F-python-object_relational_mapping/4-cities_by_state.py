#!/usr/bin/python3
"""  list all states from database """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    curso = db.cursor()
    curso.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    row = curso.fetchall()
    for x in row:
        print(x)
    curso.close()
    db.close()
