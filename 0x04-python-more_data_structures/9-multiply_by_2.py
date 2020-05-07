#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nd = dict(a_dictionary)
    for key in nd:
        nd[key] = nd[key] * 2
    return (nd)
