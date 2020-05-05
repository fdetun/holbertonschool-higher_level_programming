#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    rslt = []
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            rslt.append(True)
        else:
            rslt.append(False)
    return rslt
