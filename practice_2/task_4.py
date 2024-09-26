# -*- coding: utf-8 -*-
"""
Develop a program that asks the user for an integer 4-digit number and calculates the sum of its constituent digits. For example, if the user enters the number 3141, the program should output the following result:
3 + 1 + 4 + 1 = 9

"""


def read_int(hint: str) -> int:
    while True:
        try:
            return int(input(hint))
        except ValueError:
            print("Please enter a valid integer")


n = 4
integers = [read_int(f"Enter int {i}/{n}: ") for i in range(1, n + 1)]

print(" + ".join(str(number) for number in integers), "=", sum(integers))
