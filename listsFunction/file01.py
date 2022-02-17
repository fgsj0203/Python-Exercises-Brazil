"""
Author = Francisco Gomes
Date = 17/02/2022
description = Five numbers stored in list
version = 1.0
"""


# Creating variables and lists
numbers = [] # list empty


# Structure logical for add number in list
for x in range(0,5):
    number = int(input("Number: "))
    numbers.append(number)

# Displaying numbers of list
print("List of five numbers is: ", numbers)