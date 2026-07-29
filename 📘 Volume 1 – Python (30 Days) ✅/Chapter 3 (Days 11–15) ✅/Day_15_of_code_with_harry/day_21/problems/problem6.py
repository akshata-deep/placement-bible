
# Question 6 — Deadly Moderate 🏢 (Capgemini Style)
# 📌 Problem: Calculator Using Functions

# Create separate functions for:

# Addition
# Subtraction
# Multiplication
# Division

# Use a menu to let the user choose the operation.

# Challenge: Use return instead of print() inside each operation function.


def addition(num1,num2):
    add = num1 +num2
    return add

def subtraction(num1,num2):
    sub = num1 - num2
    return sub

def multiplication(num1,num2):
    mul = num1 *num2
    return mul

def division(num1,num2):
    div = num1/num2
    return div


num1 = int(input("Enter the 1st number : "))
num2 = int(input("Enter the 2st number : "))
option = int(input("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division \n "))
if option == 1:
    result = addition(num1,num2)
    print(f"The Result is : {result}")
elif option == 2:
    result = subtraction(num1,num2)
    print(f"The Result is : {result}")
elif option == 3:
    result = multiplication(num1,num2)
    print(f"The Result is : {result}")
elif option == 4:
    result = division(num1,num2)
    print(f"The Result is : {result}")
else:
    print("invalid option!")