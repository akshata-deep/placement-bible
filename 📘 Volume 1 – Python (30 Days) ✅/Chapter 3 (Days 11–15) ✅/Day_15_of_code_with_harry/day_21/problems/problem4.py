# Question 4 — Deadly Medium 🏢 (Infosys Style)
# 📌 Problem: Even or Odd

# Create a function that:

# Accepts one integer.
# Returns "Even" or "Odd".
# Print the result outside the function.

def even_or_odd():
    number = int(input("Enter the number : "))
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


result = even_or_odd()
print(f"the number is : {result}")