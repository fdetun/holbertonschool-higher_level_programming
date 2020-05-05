#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lena = len(tuple_a)
    lenb = len(tuple_b)
    a1 = tuple_a[0] if lena >= 1 else 0
    b1 = tuple_b[0] if lenb >= 1 else 0
    a2 = tuple_a[1] if lena >= 2 else 0
    b2 = tuple_b[1] if lenb >= 2 else 0
    f = (a1 + b1, a2 + b2)
    return f
