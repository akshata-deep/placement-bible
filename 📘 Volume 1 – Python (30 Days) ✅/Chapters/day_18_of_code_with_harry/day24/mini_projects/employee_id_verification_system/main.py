# 📌 Project: Employee ID Verification System
# Objective

# Practice tuples, indexing, in, index(), and tuple immutability.

# Requirements

# Create a tuple containing 10 Employee IDs.

# Example:

# employee_ids = (
#     "EMP101",
#     "EMP102",
#     ...
# )

# The program should display this menu:

# ===== Employee ID Verification =====

# 1. View Employee IDs
# 2. Search Employee ID
# 3. Show Total Employees
# 4. Exit
# Functionalities
# Option 1

# Display all employee IDs.

# Option 2

# Ask the user:

# Enter Employee ID:

# If found:

# Employee Found
# Index : __

# Otherwise:

# Employee Not Found
# Option 3

# Display

# Total Employees : __

# using len().

# Option 4

# Exit the program.


def view(employee_ids):
    print(employee_ids)



def search(employee_ids):
    new_id = input("Enter the id : ")
    if new_id in employee_ids:
        print(f"Employee Found\n"
              f"Index : {employee_ids.index(new_id)}")
    else:
        print("Employee Not Found")


def total(employee_ids):
    print(f"Total Employees : {len(employee_ids)}")
    





employee_ids = ("EMP001", "EMP002", "EMP003", "EMP004", "EMP005", "EMP006", "EMP007", "EMP008", "EMP009", "EMP010")

print("===== Employee ID Verification =====\n"
      "1. View Employee IDs\n"
      "2. Search Employee ID\n"
      "3. Show Total Employees\n"
      "4. Exit\n")


while True:
    option = int(input("Enter the option : "))
    if option == 1:
        view(employee_ids)
    elif option == 2:
        search(employee_ids)
    elif option == 3:
        total(employee_ids)
    elif option == 4:
        break
    else:
        print("invalid option !")