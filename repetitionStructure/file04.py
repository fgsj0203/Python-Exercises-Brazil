"""
Author = Francisco Gomes
Date = 17/02/2022
description = Five numbers and printing bigger
version = 1.0
"""
# Attribute initial number for received bigger
bigger = 0

# Structure logical repetition for attribute bigger number
for x in range(0,5):
    number = int(input("number: "))
    if (number > bigger):
        bigger = number

# Printing bigger number
print("Bigger number is: %.2f" %(bigger))

