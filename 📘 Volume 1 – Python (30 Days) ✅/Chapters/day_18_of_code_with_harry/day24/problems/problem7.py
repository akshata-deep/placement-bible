# 7. High – Student Search System

# Question:

# Create a tuple containing 8 student names.

# Requirements:

# Display all students with serial numbers.
# Ask the user to enter a student's name.
# If found:
# Print "Student Found"
# Print its index.
# Otherwise print "Student Not Found".


name = ("Akshata", "Amrita", "Prema", "Shanti", "Rahul", "Amit", "Priya", "Neha")
new_name = input("Enter the name : ")
if new_name in name:
    print("Student Found")
    print(f"its index is : {name.index(new_name)}")
else:
    print("Student Not Found")
