# 5. Age validation

# Ask the user for age.

# If age is below 18, raise:

# You must be 18 or above.

age = int(input("Enter your age : "))
if age < 18:
    raise ValueError("You Must Be 18 OR Above")
print("Done")