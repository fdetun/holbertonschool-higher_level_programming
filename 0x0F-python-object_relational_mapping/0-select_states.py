#!/usr/bin/python3
"""
tsk0
"""

import MySQLdb as mdb
import sys


def byfoued():
    fdb = mdb.connect(host='localhost',
                      port=3306,
                      user=sys.argv[1],
                      passwd=sys.argv[2],
                      db=sys.argv[3]
                      )
    cursor = fdb.cursor()
    cursor.execute('SELECT * FROM states ORDER BY id ASC')
    for i in cursor:
        print(i)


if __name__ == "__main__":
    byfoued()
