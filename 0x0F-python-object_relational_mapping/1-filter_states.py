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
    fd = cursor.fetchall()
    for i in fd:
        print(i)
    cursor.close()
    fdb.close()

if __name__ == "__main__":
    byfoued()
