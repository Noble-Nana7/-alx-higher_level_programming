#!/use/bin/python3

from calculator_1 import add, subtract, multiply, divide

if __name__ == "__main__":

    a = 10
    b = 5

    r_add = add(a, b)
    r_minus = subtract(a, b)
    r_mul = multiply(a, b)
    r_div = divide(a, b)

    print("{} + {} = {}".format(a, b, r_add))
    print("{} - {} = {}".format(a, b, r_minus))
    print("{} * {} = {}".format(a, b, r_mul))
    print("{} / {} = {}".format(a, b, r_div))
