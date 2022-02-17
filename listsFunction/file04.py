"""
Author = Francisco Gomes
Date = 17/02/2022
description = list with 20 numbers and display in list of odd and pair
version = 1.0
"""

# Creating lists and variables
listNumbers = []
listPair = []
listOdd = []

# Structure logical for operation numbers separate odd and pair
for x in range(0,20):
    number=int(input("Number: "))
    listNumbers.append(number)
    if(number % 2 == 0):
        listPair.append(number)
    else:
        listOdd.append(number)

# Displaying lists of all numbers, Pair and Odd
print("List of all numbers: ", listNumbers)
print("List of pair numbers: ", listPair)
print("List of Odd numbers: ", listOdd)

