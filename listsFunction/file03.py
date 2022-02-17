"""
Author = Francisco Gomes
Date = 17/02/2022
description = list with 10 character and display only consonant and count
version = 1.0
"""

# Creating list and variables
listLetters = []
listConsonant = []
# Structure logical for add letters in list and operation of identify letters consonant
for x in range(0,10):
    letter = str(input("Letter: "))
    letterConverter = letter.lower() # Forced converter letter for lowercase
    listLetters.append(letter)
    if(letter != "a" and letter != "e" and letter != "i" and letter != "o" and letter != "u"):
        listConsonant.append(letter)


# Displaying list of all letters and list of only consonant
print("List of letters is: ", listLetters)
print("List only letters consonant is: ",listConsonant)




