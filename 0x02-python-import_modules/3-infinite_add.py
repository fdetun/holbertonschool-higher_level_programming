#!/usr/bin/python3
if __name__ == "__main__":
    addition = 0
    from sys import argv
    for i in range(1,len(argv)):
        addition = addition + int(argv[i])
    print("{:d}".format(addition))
