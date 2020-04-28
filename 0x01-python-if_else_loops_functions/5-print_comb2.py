#!/usr/bin/python3
for f in range(0, 100):
    if f != 99:
        print("{:02d}".format(f), end=", ")
    else:
        print("{:02d}".format(f))
