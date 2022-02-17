"""
Author = Francisco Gomes
Date = 17/02/2022
description = Identify day of week with number
version = 1.0
"""

# Variable
numberDay = int(input("Enter with a number: "))

# Operation Logical identify day of week
if(numberDay == 1):
    print("Sunday")
elif(numberDay == 2):
    print("Monday")
elif(numberDay == 3):
    print("Tuesday")
elif(numberDay == 4):
    print("Wednesday")
elif(numberDay == 5):
    print("Thursday")
elif(numberDay == 6):
    print("Friday")
elif(numberDay == 7):
    print("Saturday")
elif(numberDay < 1 or numberDay > 7):
    print("Day invalid, try again")