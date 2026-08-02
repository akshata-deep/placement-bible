# Q4 — Medium

# Create three functions:

# add()
# subtract()
# multiply()

# Give each function its own docstring.

# Print the docstring of each function.


def add(num1,num2):
    "it will take the num1 and num2 value and print the sum of that "
    sum = num1 + num2
    return sum


def  subtract(num1,num2):
    "it will take the num1 and num2 value and print the subtarction of that "
    sub = num1 - num2
    return sub


def multiply(num1,num2):
    "it will take the num1 and num2 value and print the multiplication of that "
    mul = num1 + num2
    return mul

print(add.__doc__)
print(subtract.__doc__)
print(multiply.__doc__)
