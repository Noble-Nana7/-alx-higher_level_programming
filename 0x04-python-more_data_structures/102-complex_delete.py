#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if a_dictionary is None or not isinstance(a_dictionary, dict):
    return  # or handle the error accordingly


    keys = [key for key, val in a_dictionary.items() if val == value]
    for key in keys:
        del a_dictionary[key]
