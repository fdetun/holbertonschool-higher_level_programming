#!/usr/bin/python3
"""
upper N
"""

import MySQLdb as mdb
import sys


def byfoued():
    """
    function by foued
    """
    fdb = mdb.connect(host='localhost',
                      port=3306,
                      user=sys.argv[1],
                      passwd=sys.argv[2],
                      db=sys.argv[3]
                      )
    cursor = fdb.cursor()
    cursor.execute(
        """SELECT * FROM states WHERE states.name LIKE 'N%' ORDER BY id ASC""")
    for i in cursor:
        print(i)


if __name__ == "__main__":
    byfoued()
