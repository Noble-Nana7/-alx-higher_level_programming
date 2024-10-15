#!/usr/bin/python3

import sys

if __name__ == "__main__":

    arg = sys.argv[1:]
    lenarg = len(arg)

    if lenarg == 0:
        print(f"{lenarg} arguments.")
    elif lenarg == 1:
        print(f"{lenarg} argument:")
    else:
        print(f"{lenarg} arguments:")

    for i in range(len(arg)):
        print(f"{i+1}: {arg[i]}")
