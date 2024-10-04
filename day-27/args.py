from turtle import mode
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


class Car:

    def __init__(self, **kwargs) -> None:
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")


volvo_car = Car(make="Volvo", model="S-90")
print(volvo_car)
