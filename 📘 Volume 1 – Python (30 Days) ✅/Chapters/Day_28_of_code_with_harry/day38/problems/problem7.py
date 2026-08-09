# Day 38 Challenge ⭐

# Create a program that accepts:

# Enter a number between 5 and 9:

# If the user enters:

# 5–9 → continue
# quit → exit normally
# any other string → show an appropriate error





try:
    a = int(input("Enter a number between 5 and 9:"))
    if a <5 or a>9:
            raise ValueError("value must be between 5 and 9")
    print("valid")

except Exception as e:
    print(e)