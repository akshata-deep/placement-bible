# Question 7 — High (IBM Style)
# 📌 Problem: Student Result Analyzer

# Create a list of five student marks.

# Your program should:

# Print all marks.
# Print the highest mark.
# Print the lowest mark.
# Check whether a user-entered mark exists in the list.
# Print "Found" or "Not Found".

marks = [10,20,30,40,50]
number = int(input("Enter the marks :"))
print(marks)
print(max(marks))
print(min(marks))
if number in marks:
    print("Found")
else:
    print("Not Found")