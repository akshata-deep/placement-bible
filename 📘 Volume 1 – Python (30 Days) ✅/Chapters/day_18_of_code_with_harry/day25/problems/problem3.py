# Medium

# Create a tuple of 10 employee IDs.

# Ask the user to enter an employee ID.

# If found:

# Print "Employee Found"
# Print its index

# Otherwise print:

# Employee Not Found

employee_ids = (1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010)
new = int(input("enter the new :"))
if new in employee_ids:
    print("Employee Found")
else:
    print("not found")
