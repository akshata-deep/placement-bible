# Question 6 — Deadly Moderate (Accenture Style)
# 📌 Problem: Even Number Checker

# Create a list:

# 12, 15, 18, 21, 24, 27, 30

# Using a loop:

# Print only the even numbers.
# Count how many even numbers are present.
# Print the final count


l1 = [12, 15, 18, 21, 24, 27, 30]
even = [i for i in l1 if i%2 ==0]
print(even)
print(len(even))
print(len(l1))