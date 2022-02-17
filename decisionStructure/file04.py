"""
Author = Francisco Gomes
Date = 16/02/2022
description = verify letter if vowel or consonant
version = 1.0
"""

# Variables and input data
letter = str(input("Input a letter: "))

# Converting value string in lowercase
converterLetter = letter.lower()

# Structure logical decision
if (converterLetter != "a" and converterLetter != "e" and converterLetter != "i" and converterLetter != "o" and converterLetter != "u"):
    print("You letter is consonant")
    print("You letter: ", converterLetter)
else:
    print("Letter is vowel")
    print("You letter: ", converterLetter)