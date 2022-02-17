"""
Author = Francisco Gomes
Date = 16/02/2022
description = indicate which time of day
version = 1.0
"""

# Variables
timeDay = str(input("Enter with time of day: "))

# Return identify time day with first letter
identifyTimeDay = timeDay.capitalize()

# Converting the character for lowercase
converterTimeDay = identifyTimeDay.lower()

# Structure logical development for identify time day
if(converterTimeDay == "m"):
    print("Morning time")
elif(converterTimeDay == "v"):
    print("Afternoon time")
elif(converterTimeDay == "n"):
    print("Night time")
else:
    print("Time day invalid, try again")

