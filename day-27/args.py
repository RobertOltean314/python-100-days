from numpy import multiply


def add(*args):
    sum = 0
    for number in args:
        sum += number
    return sum


def calculate(number, **kwargs):
    # for key, value in kwargs:
    #     print(key)
    #     print(value)
    number += kwargs["add"]
    number *= kwargs["multiply"]
    print(number)


calculate(2, add=3, multiply=5)
