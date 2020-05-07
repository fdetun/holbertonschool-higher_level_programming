#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nl = my_list[:]
    for i in nl:
        if i == search:
            a = nl.index(i)
            nl.remove(i)
            nl.insert(a, replace)
    return (nl)
