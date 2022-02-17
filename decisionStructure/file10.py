"""
Author = Francisco Gomes
Date = 17/02/2022
description = Calculate readjustment under salary
version = 1.0
"""

# Variables
valueHourWork = float(input("Value of hour work: "))
hoursWorkedMonth = int(input("What hours in month: "))

# Calculating salary brute
salaryBrute = (valueHourWork * hoursWorkedMonth)
print("Salary brute is: R$%.2f" %( salaryBrute ))

# Development structure logical of status tax and discounts
# Calculating discounts and display salary liquid
if (salaryBrute <= 900):
    print("You is free of taxes and discounts")
    print("You salary brute is: R$%.2f" %(salaryBrute))
elif(salaryBrute > 900 and salaryBrute <= 1500):
    discountIR = (salaryBrute*0.05)
    discountINSS = (salaryBrute*0.10)
    bonusFGTS = (salaryBrute*0.11)
    totalDiscounts = (discountIR + discountINSS)
    print("Discount of IR is: %.2f" %(discountIR))
    print("Discount of INSS is: %.2f" %(discountINSS))
    print("Discount of you bonus FGTS: %.2f" %(bonusFGTS))
    print("Total discounts is: ", totalDiscounts)
    print("You salary liquid is: %.2f" %(salaryBrute - totalDiscounts))
elif(salaryBrute > 1500 and salaryBrute <= 2500):
    discountIR = (salaryBrute*0.10)
    discountINSS = (salaryBrute*0.10)
    bonusFGTS = (salaryBrute*0.11)
    totalDiscounts = (discountIR + discountINSS)
    print("Discount of IR is: %.2f" %(discountIR))
    print("Discount of INSS is: %.2f" %(discountINSS))
    print("Discount of you bonus FGTS: %.2f" %(bonusFGTS))
    print("Total discounts is: ", totalDiscounts)
    print("You salary liquid is: %.2f" %(salaryBrute - totalDiscounts))
elif(salaryBrute > 2500):
    discountIR = (salaryBrute*0.20)
    discountINSS = (salaryBrute*0.10)
    bonusFGTS = (salaryBrute*0.11)
    totalDiscounts = (discountIR + discountINSS)
    print("Discount of IR is: %.2f" %(discountIR))
    print("Discount of INSS is: %.2f" %(discountINSS))
    print("Discount of you bonus FGTS: %.2f" %(bonusFGTS))
    print("Total discounts is: ", totalDiscounts)
    print("You salary liquid is: %.2f" %(salaryBrute - totalDiscounts))