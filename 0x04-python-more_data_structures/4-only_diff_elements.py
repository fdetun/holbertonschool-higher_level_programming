#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    notCommon = set_1 ^ set_2
    return notCommon
