#!/usr/bin/python3
i = 0
j = 0
for k in range(0, 45):
    j = j + 1
    print("{}{}".format(i, j), end=", ")
    if j == 9:
        i = i + 1
        if i == 8:
            print("{}{}".format(i, j))
        j = i
