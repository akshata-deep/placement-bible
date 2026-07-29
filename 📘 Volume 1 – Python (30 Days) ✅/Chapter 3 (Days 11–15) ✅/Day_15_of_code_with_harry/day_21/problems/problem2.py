# Question 2 — Deadly Easy
# 📌 Problem: Find the Square

# Write a function that:

# Accepts one number.
# Returns its square.
# # Print the returned value in the main program.

def square(num):
    sum = num**2
    return sum


num = int(input("Enter the number : "))
sum = square(num)
print(f"The Square of the number is : {sum}")