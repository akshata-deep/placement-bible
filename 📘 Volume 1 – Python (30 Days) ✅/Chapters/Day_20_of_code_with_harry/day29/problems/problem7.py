# Q7 — High

# Create a Student Result System.

# Functions:

# calculate_total()
# calculate_average()
# check_result()

# Each function must contain a meaningful docstring.


def calculate_total(number1, number2):
    """ INPUT : it will take 2(number1 and number2) numbers \nPURPOSE : this fuction is use to calculte the sum of the numbers \nRETURN VALUE : it will return the sum of numbers values"""
    add  = number1 + number2
    print(add)
    return add


def calculate_average():
    """ INPUT : it will take 2(number1 and number2) numbers \nPURPOSE : this fuction is use to subtract the 2 numbers \nRETURN VALUE : it will return the subtraction of numbers values"""
    average = (number1 + number2) / 2
    print(average)
    return average


def check_result(total, average):
    print(" =============== Student result system =============== \n"
          f"TOTAL : {total}\n"
          f"AVERAGE : {average}\n"
          "--------------------------------------\n"
          )





number1 = int(input("Enter the number 1 : "))
number2 = int(input("Enter the number 2 : "))


print("1.total\n"
      "2.average\n"
      "3.result\n"
      "4.exit")

while True:
    option = int(input("Enter the option : "))
    if option == 1:
        total = calculate_total(number1,number2)
    elif option == 2:
        average = calculate_average()
    elif option == 3:
        check_result(total, average)
    elif option == 4:
        break
    else:
        print("invlaid option !")