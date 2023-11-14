# print_operations.py

from math_operations import add, subtract, multiply, divide


def print_operations(a, b):
    print(f"The sum of {a} and {b} is {add(a, b)}")
    print(f"The difference between {a} and {b} is {subtract(a, b)}")
    print(f"The product of {a} and {b} is {multiply(a, b)}")
    print(f"The division of {a} by {b} results in {divide(a, b)}")
