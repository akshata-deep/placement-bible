# Q3 — Division

# Ask the user for two numbers and divide them.

# Handle the error if the input is invalid.


try:
    num1 = int(input("Enter the number 1: "))
    num2 = int(input("Enter the number 2: "))
    print(f"{num1/num2:.2f}")
except:
    print(f"{num2} is Invalid value ")