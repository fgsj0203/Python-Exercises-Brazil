"""
Author = Francisco Gomes
Date = 17/02/2022
description = Ten numbers stored in list and displaying inverse
version = 1.0
"""

# Creating list empty
listNumber = []

# Structure logical for add number in list
for x in range(0,10):
    numbers=float(input("Number: "))
    listNumber.append(numbers)

# Displaying number inverse
print(listNumber[::-1])




