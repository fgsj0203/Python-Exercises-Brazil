"""
Author = Francisco Gomes
Date = 17/02/2022
description = Five numbers and printing bigger
version = 1.0
"""

# Structure logical for calculate average numbers
sumNumbers = 0

for x in range(0,5):
    number = int(input("Number: "))
    sumNumbers += number

# Calculating average of numbers
averageNotes = sumNumbers / 5

# Displaying average and sum of notes

print("This average of notes is: ", averageNotes)
print("The sum of numbers is: ", sumNumbers)
