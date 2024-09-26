# -*- coding: utf-8 -*-
"""
Develop a program that asks the user for an integer 4-digit number and calculates the sum of its constituent digits. For example, if the user enters the number 3141, the program should output the following result:
3 + 1 + 4 + 1 = 9

"""


def read_4_digit_int() -> int:
    while True:
        try:
            number = int(input("Enter an integer 4-digit number: "))
        except ValueError:
            print("Please enter a valid integer")
        else:
            if 1000 <= number <= 9999:
                return number
            print("Please enter an integer 4-digit number")

number = read_4_digit_int()

digits = []
while number > 0:
    digits.append(number % 10)
    number = number // 10

print(" + ".join(str(digit) for digit in digits[::-1]), "=", sum(digits))
