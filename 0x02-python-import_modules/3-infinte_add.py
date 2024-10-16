#!/usr/bin/python3

import sys
if __name__ == "__main__":

    arg = sys.argv[1:]
    lenarg = len(arg)
    sumarg = 0

    if lenarg > 0:
        for i in arg:
            sumarg += int(i)
    print(sumarg)
