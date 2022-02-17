"""
Author = Francisco Gomes
Date = 16/02/2022
description = Calculate readjustment under salary
version = 1.0
"""

# Variables
salary = float(input("Salary: "))
readjustmentSalary = 0


# Structure decision for calculate readjustment under salary
if (salary <= 280):
    print("Readjusment of salary is 20%")
    print("Value of readjustment is: %.2f" %(salary * 0.20))
    readjustmentSalary = (salary + (salary * 0.20))
    print("you salary with readjustment is: R$%.2f" %(readjustmentSalary))
elif (salary > 280 and salary <= 700):
    print("Readjusment of salary is 15%")
    print("Value of readjustment is: %.2f" %(salary * 0.15))
    readjustmentSalary = (salary + (salary * 0.15))
    print("you salary with readjustment is: R$%.2f" %(readjustmentSalary))
elif (salary > 700 and salary <= 1500):
    print("Readjusment of salary is 10%")
    print("Value of readjustment is: %.2f" %(salary * 0.10))
    readjustmentSalary = (salary + (salary * 0.10))
    print("you salary with readjustment is: R$%.2f" %(readjustmentSalary))
elif (salary > 1500):
    print("Readjusment of salary is 5%")
    print("Value of readjustment is: %.2f" %(salary * 0.05))
    readjustmentSalary = (salary + (salary * 0.05))
    print("you salary with readjustment is: R$%.2f" %(readjustmentSalary))