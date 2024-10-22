#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list != " ":
        for i in my_list:
            if i * 2 > 100:
                return i
    else:
        return None
