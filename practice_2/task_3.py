# -*- coding: utf-8 -*-
"""
Write a program to calculate the body mass index (BMI) of a person. The user must enter their height and weight, after which you use one of the formulas below to determine the index.
BMI = weight/height**2 
"""


def read_float(hint: str) -> float:
    while True:
        try:
            return float(input(hint))
        except ValueError:
            print("Please enter a valid number")


weight = read_float("Enter weight in kg: ")
height = read_float("Enter height in cm: ") / 100

bmi = weight / height ** 2

print(f"Calcaulated BMI: {bmi:.2f}")
