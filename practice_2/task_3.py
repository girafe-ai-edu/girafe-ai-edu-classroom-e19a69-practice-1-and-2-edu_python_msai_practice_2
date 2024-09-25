# -*- coding: utf-8 -*-
"""
Write a program to calculate the body mass index (BMI) of a person. The user must enter their height and weight, after which you use one of the formulas below to determine the index.
 = weight/height**2 
"""
weight = float(input())
height = float(input())

#code here
BMI =  weight/height**2
print(BMI)