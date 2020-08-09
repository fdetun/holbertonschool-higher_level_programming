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
    cmd = "SELECT cities.name FROM cities JOIN states ON\
                 cities.state_id = states.id WHERE states.name \
                 LIKE '{}' ORDER BY cities.id".format(sys.argv[4])
    cursor.execute(cmd)
    fd = cursor.fetchall()
    l=", ".join(n[0] for n in fd)
    print(l)
    cursor.close()
    fdb.close()


if __name__ == "__main__":
    byfoued()
