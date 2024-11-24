#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end='')
                count += 1
            except (ValueError, TypeError):
                continue
    except IndexError:
        raise
    finally:
        print()
    return count

my_list = [1, 2, 3, 4]
x = len(my_list) + 4
nb_print = safe_print_list_integers(my_list, x)
print("{:d}".format(nb_print))
