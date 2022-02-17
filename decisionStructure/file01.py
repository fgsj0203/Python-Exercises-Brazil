"""
Author = Francisco Gomes
Date = 16/02/2022
description =  input two numbers and print bigger number
version = 1.0
"""

# Variables
numberOne = int(input("First number: "))
numberTwo = int(input("Second number: "))

# Calculating of bigger number
if numberOne > numberTwo:
    print("Number one: ", numberOne)
    print("Number two: ", numberTwo)
    print("A number one is bigger, number: %.2f" %(numberOne))
else:
    print("Number one: ", numberOne)
    print("Number two: ", numberTwo)
    print("A number two is bigger, number: %.2f" %(numberTwo))


