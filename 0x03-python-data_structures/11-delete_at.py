#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    rm = idx + 1
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list.remove(rm)
    return my_list
