#!/usr/bin/python3
def uniq_add(my_list=[]):
    nl = []
    a = 0
    for i in my_list:
        if i not in nl:
            nl.append(i)
    for j in nl:
        a = a + j
    return a
