#!/usr/bin/python3
"""
from input
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
    cmd = "SELECT * FROM states"

    cursor.execute(cmd)
    fd = cursor.fetchall()

    for i in fd:
        if i[1] == sys.argv[4]:
            print(i)
    cursor.close()
    fdb.close()


if __name__ == "__main__":
    byfoued()
