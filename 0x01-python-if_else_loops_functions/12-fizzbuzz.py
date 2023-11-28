#!/usr/bin/env python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            print("Fizz", end=" " if i < 100 else "\n")
        elif i % 5 == 0:
            print("Buzz", end=" " if i < 100 else "\n")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" " if i < 100 else "\n")
        else:
            print("{}".format(i), end=" " if i < 100 else "\n")

fizzbuzz()
