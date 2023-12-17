#!/usr/bin/python3
"""  lists all states from database  """
import MySQLdb
import sys


if __name__ == "__main__":
    datab = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    curs = datab.cursor()
    curs.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    datab.close()
