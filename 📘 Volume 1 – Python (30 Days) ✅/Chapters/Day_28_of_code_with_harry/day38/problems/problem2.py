# 2. Range validation

# Ask the user for a number between 5 and 9.

# 5–9 → continue
# Anything else → raise ValueError

a = int(input("Enter the num in between 5 and 9 : "))
if a>5 and a<9:
    raise ValueError
print("continue")