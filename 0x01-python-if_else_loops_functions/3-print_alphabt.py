#!/usr/bin/python3
for f in range(97, 123):
    if f == 101 or f == 113:
        continue
    print("{:c}".format(f), end='')
