# Take:

# first number
# second number
# operator (+, -, *, /)

# Use match-case to perform the correct operation.

number1 = int(input("Enter the 1st number :"))
number2 = int(input("Enter the 2st number :"))
operator = input(f"Enter the operator which you what to perform :")

match operator:
    case "+":
        print(number1 + number2)
    case "-":
        print(number1 - number2)
    case "*":
        print(number1 * number2)
    case "/":
        print(number1 / number2)
    case _:
        print("invalid")