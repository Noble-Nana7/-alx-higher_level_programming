#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Use 0 if the tuple has fewer than 2 elements,
    # otherwise use its actual values
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0
    # Add the corresponding elements from both tuples and return a new tuple
    return (a1 + b1, a2 + b2)
