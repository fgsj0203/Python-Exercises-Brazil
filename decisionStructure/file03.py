"""
Author = Francisco Gomes
Date = 16/02/2022
description = verify gender Male or Female
version = 1.0
"""

# Variables
gender = str(input("indicate you gender: "))

# Converting value String for lowercase
converterString = gender.lower()

# Structure logical decision
if (converterString == "f"):
    print("You gender is female")
elif (converterString == "m"):
    print("You gender is male")
else:
    print("Yout gender is other")
