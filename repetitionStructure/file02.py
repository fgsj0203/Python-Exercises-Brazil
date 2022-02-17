"""
Author = Francisco Gomes
Date = 17/02/2022
description = Calculate readjustment under salary
version = 1.0
"""

# Variables
user = str(input("You profile: "))
password = str(input("You password: "))

# Structure logical repetition for validate profile and password
while(user == password):
    print("Content User and password is equal, not permitted")
    user = str(input("You profile: "))
    password = str(input("You password: "))

# Displaying values of User and Password
print("You profile is: ", user)
print("You password is: ", password)