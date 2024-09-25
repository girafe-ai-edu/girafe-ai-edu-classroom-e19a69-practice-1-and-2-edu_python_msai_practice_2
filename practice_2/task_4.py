# -*- coding: utf-8 -*-
"""
Develop a program that asks the user for an integer 4-digit number and calculates the sum of its constituent digits. For example, if the user enters the number 3141, the program should output the following result:
3 + 1 + 4 + 1 = 9

"""

while 1==1:
    try:
        number = int(input('\n' + "Введите любое 4-х значное число" + '\n'))
        if (999 < number < 10000):
            break
    except:
        print("Попробуй ещё раз")

print(number % 10 + number // 10 % 10 + number // 100 % 10 + number // 1000)