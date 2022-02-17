"""
Author = Francisco Gomes
Date = 17/02/2022
description = Input note between zero and ten
version = 1.0
"""


# Variables
note = int(input("Enter with note: "))

# Structure repetition for input note invalid
while(note < 0 or note > 10):
    print("Note invalid, try again")
    note = int(input("Enter with a note again: "))

# Displaying note valid
print("Note is: ", note)