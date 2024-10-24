#!/usr/bin/python3

new_list = []

def search_replace(my_list, search, replace):
    for idx in range(len(my_list)):
        if my_list[idx] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[idx])

    return new_list
        
