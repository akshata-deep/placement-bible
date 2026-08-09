# 1. Basic raise

# Ask the user for a number.

# If the number is less than 5, raise a ValueError.

a = int(input("Enter the number : "))
if a < 5:
    raise ValueError

print("Done")