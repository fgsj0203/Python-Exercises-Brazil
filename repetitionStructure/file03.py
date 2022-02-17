"""
Author = Francisco Gomes
Date = 17/02/2022
description = Input note between zero and ten
version = 1.0
"""

# Structure logical for validate input data
name = str(input("Enter with a name: "))
while(len(name) < 3):
    print("Name need more three characters")
    name = str(input("Enter again with a name: "))

age = int(input("Enter with a age: "))
while(age < 0 or age > 150):
    print("Age need between 0 and 150")
    age = int(input("Enter again with a age: "))

salary = float(input("Enter with salary: "))
while(salary < 0):
    print("You salary need more zero")
    salary = float(input("Enter with salary: "))

gender = str(input("Enter with you gender: "))
letterLower = gender.lower()
print(letterLower)
while(letterLower != "f" and letterLower != "m"):
    print("Gender other")
    gender = str(input("Enter again you gender: "))
    converterLetterGender = gender.lower()

maritalState = str(input("You Status marital: "))
firstLetter = maritalState.capitalize()
firstLetterLower = firstLetter.lower()
while(firstLetterLower != "s" and firstLetterLower != "c" and firstLetterLower != "v" and firstLetterLower != "d"):
    print("marital state invalid, try again!")
    maritalState = str(input("You Status marital: "))
    firstLetter = maritalState.capitalize()
    firstLetterLower = firstLetter.lower()

# ------------------------------------------------------------------------------------
# Displaying values valid of variables

print("------------------------------------------------------------------------------")
print("Name is: ", name)
print("Age is: ", age)
print("Salary is: ", salary)
print("Gender is: ", letterLower)
print("Status Marital is: ", firstLetterLower)



