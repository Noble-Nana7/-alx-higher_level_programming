#!/usr/bin/python3
import random
number = random.randint(-10, 10)

match number:
    case x if x < 0:
        print(f"{x} is negative")
    case x if x == 0:
        print(f"{x} is zero")
    case x if x > 0:
        print(f"{x} is positive")
