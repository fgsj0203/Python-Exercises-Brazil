"""
Author = Francisco Gomes
Date = 16/02/2022
description = verify is bigger three numbers
version = 1.0
"""

# Variables
numberOne = int(input("Number one: "))
numberTwo = int(input("Number two: "))
numberThree = int(input("Number three: "))

# Logical structure development (First method)
biggerNumber = max(numberOne, numberTwo, numberThree)

# Displaying bigger number using function "max"
print("Bigger number is: %.2f" %(biggerNumber))

# Logical structure development (Second method)
if(numberOne > numberTwo and numberOne > numberThree and numberTwo > numberThree):
    print("Bigger number is one: ", numberOne)
elif(numberTwo > numberThree and numberTwo > numberOne and numberThree > numberOne):
    print("Bigger number is two: ", numberTwo)
elif(numberThree > numberOne and numberThree > numberTwo and numberOne > numberTwo):
    print("Bigger number is three: ", numberThree)



