#!/usr/bin/python3
def best_score(a_dictionary):
    rslt=""
    if a_dictionary is None or a_dictionary is {}:
        return None
    else:
        maxi = sorted(a_dictionary.values())
        key = list(a_dictionary.keys())
        for i in key:
            if a_dictionary[i] == maxi[len(maxi) - 1] :
                rslt = i
    return rslt
