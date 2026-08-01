# Q6 — Moderate

# Create a small calculator with functions:

# addition
# subtraction
# multiplication
# division

# Give every function a meaningful docstring.

# Try to keep the code PEP 8 friendly.

def addition(number1, number2):
    """ INPUT : it will take 2(number1 and number2) numbers \nPURPOSE : this fuction is use to calculte the sum of the numbers \nRETURN VALUE : it will return the sum of numbers values"""
    add  = number1 + number2
    print(add)


def subtraction(number1, number2):
    """ INPUT : it will take 2(number1 and number2) numbers \nPURPOSE : this fuction is use to subtract the 2 numbers \nRETURN VALUE : it will return the subtraction of numbers values"""
    sub  = number1 - number2
    print(sub)


def multiplication(number1, number2):
    """ INPUT : it will take 2(number1 and number2) numbers \nPURPOSE : this fuction is use to multiply the numbers \nRETURN VALUE : it will return the result of multiplication  result"""
    mul  = number1 * number2
    print(mul)

def division(number1, number2):
    """ INPUT : it will take 2(number1 and number2) numbers \nPURPOSE : this fuction is use to division the numbers\n and also if the number 2 is 0 means it will tell that \"this number by 0 is undefined\" \nRETURN VALUE : it will return the result of division result"""
    if number2 == 0:
        print(f"{number1} divided by 0 is undefined.")
    else:
        div  = number1 / number2
        print(div)






number1 = int(input("Enter the number 1 : "))
number2 = int(input("Enter the number 2 : "))


print("1.addition\n"
      "2.subtraction\n"
      "3.multiplication\n"
      "4.division\n"
      "5.exit")

while True:
    option = int(input("Enter the option : "))
    if option == 1:
        addition(number1,number2)
    elif option == 2:
        subtraction(number1,number2)
    elif option == 3:
        multiplication(number1,number2)
    elif option == 4:
        division(number1,number2)
    elif option == 5:
        break
    else:
        print("invlaid option !")