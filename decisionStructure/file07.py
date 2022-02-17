"""
Author = Francisco Gomes
Date = 16/02/2022
description = verify is bigger and smaller of three numbers
version = 1.0
"""

# Variables
numberOne = int(input("Number one: "))
numberTwo = int(input("Number two: "))
numberThree = int(input("Number three: "))

# ---------------------------------------------------------------------------
# First method of verify bigger and smaller number
biggerNumber = max(numberOne, numberTwo, numberThree)
smallerNumber = min(numberOne, numberTwo, numberThree)

# Displaying of bigger and smaller number
print("Bigger number is: %.1f" %(biggerNumber))
print("Smaller number is: %.1f" %(smallerNumber))

# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Displaying bigger and smaller number (second method)
if (numberOne > numberTwo and numberOne > numberTwo and numberTwo > numberThree):
    print("Bigger number is: ",numberOne)
    print("Smaller number is: ",numberThree)
elif(numberTwo > numberThree and numberTwo > numberOne and numberThree > numberOne):
    print("Bigger number is: ",numberTwo)
    print("Smaller number is: ",numberOne)
elif(numberThree > numberOne and numberThree > numberTwo and numberOne > numberTwo):
    print("Bigger number is: ",numberThree)
    print("Smaller number is: ",numberTwo)

