"""
Author = Francisco Gomes
Date = 16/02/2022
description = verify letter if vowel or consonant
version = 1.0
"""

# Variables with First validation of note value
noteOne = float(input("Note one: "))
if(noteOne < 0 or noteOne > 10):
    print("Input invalid, try again")
    noteOne = float(input("Note one: "))

noteTwo = float(input("Note two: "))
if(noteTwo < 0 or noteTwo > 10):
    print("Input invalid, try again")
    noteTwo = float(input("Note two: "))

# logical structure development average notes
# Calculating average notes
averageNotes = (noteOne + noteTwo) / 2

# Logical structure of decision average and status
if (averageNotes >= 7 and averageNotes <= 9.9):
    print("You approved, congratulation")
    print("You average is: %.2f" %(averageNotes))
elif(averageNotes < 7):
    print("You reproved, try again")
    print("You average is: %.2f" %(averageNotes))
elif(averageNotes == 10.0):
    print("You approved with distinction, Happy party")
    print("You average is: %.2f" %(averageNotes))
