# Q5 — Moderate

# Create a function that calculates the average of three marks.

# Your docstring should explain:

# Input
# Purpose
# Return value

# Then print the docstring.


def average(*number):
    """ INPUT : it will take n numbers \nPURPOSE : this fuction is use to calculte the average of the numbers \nRETURN VALUE : it will return the average of n values"""
    total = sum(number)
    avg = total / len(number)
    return total



print(average.__doc__)