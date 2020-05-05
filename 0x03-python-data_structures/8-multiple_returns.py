#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        f = (len(sentence), None)
    else:
        f = (len(sentence), sentence[0])
    return f
