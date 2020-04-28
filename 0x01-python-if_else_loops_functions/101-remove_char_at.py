#!/usr/bin/python3
def remove_char_at(str, n):
    f = ""
    lenth = len(str)
    for i in range(0, lenth):
        if i == n:
            continue
        else:
            f = f + str[i]
    return (f)
