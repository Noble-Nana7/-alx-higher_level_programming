#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for i in r:
            print("".join({:d}".format(i)))
