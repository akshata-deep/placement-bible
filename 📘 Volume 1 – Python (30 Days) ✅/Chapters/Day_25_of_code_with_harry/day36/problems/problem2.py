# Q2 — Multiplication Table

# Create a multiplication-table program using try-except.

# If the user enters something like "Harry", display:

# Invalid input

try:
    num = int(input("Enter the number : "))
    for i in range (1,11):
        print(f"{num} X {i} = {num*i}")
except:
    print("Invalid input")
