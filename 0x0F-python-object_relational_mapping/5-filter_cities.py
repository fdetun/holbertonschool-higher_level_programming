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
    s=set()
    fdb = mdb.connect(host='localhost',
                      port=3306,
                      user=sys.argv[1],
                      passwd=sys.argv[2],
                      db=sys.argv[3]
                      )
    cursor = fdb.cursor()
    cmd = "SELECT cities.id,cities.name,states.name FROM cities join\
    states on cities.state_id=states.id"
    cursor.execute(cmd)
    fd = cursor.fetchall()
    for i in fd:
        if i[2] == sys.argv[4]:
            s.add(i[1])
    print(", ".join(x for x in s))
    cursor.close()
    fdb.close()


if __name__ == "__main__":
    byfoued()
