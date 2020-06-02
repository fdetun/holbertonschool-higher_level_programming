#!/usr/bin/python3
""" 
class Mylist
"""


class MyList(list):
    """MyList that inherits from list"""
    
    def __init__(self):
        super().__init__(self)

    def print_sorted(self):
        self.lis = self
        print(sorted(self.lis))
