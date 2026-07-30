# Day 24 — Mini Project 2 (Intermediate)
# 📌 Project: Airport Flight Code Checker
# Objective

# Build a tuple-based flight lookup system.

# Requirements

# Create a tuple containing at least 10 flight codes.

# Example:

# flights = (
#     "AI101",
#     "6E234",
#     "UK550",
#     ...
# )

# Menu:

# ===== Airport Flight System =====

# 1. View Flights
# 2. Search Flight
# 3. Show Flight Count
# 4. Slice Domestic Flights
# 5. Exit
# Functionalities
# Option 1

# Display all flight codes.

# Option 2

# Ask the user:

# Enter Flight Code:

# If found:

# Flight Available
# Index : __

# Else:

# Flight Not Found
# Option 3

# Display

# Total Flights : __
# Option 4

# Display only the first five flight codes using slicing.

# Example:

# flights[:5]
# Option 5

# Exit.

# Rules
# Use tuple only
# Use slicing
# Use index()
# Use len()
# Use in
# Use functions
# Menu-driven program


def view(flight_numbers):
    print(flight_numbers)

def search(flight_numbers):
    new_flight = input("Enter the flight number : ")
    if new_flight in flight_numbers:
        print("Found")
    else:
        print("not found")

def total(flight_numbers):
    print(f"Total Flights : {len(flight_numbers)}")

def sliceing(flight_numbers):
    print(flight_numbers[:5])



flight_numbers = ("AI101", "EK203", "BA017", "6E2104", "LH430", "QF002", "SQ321", "AA100", "DL042", "AF015")
print("===== Airport Flight System =====\n"
      "1. View Flights\n"
      "2. Search Flight\n"
      "3. Show Flight Count\n"
      "4. Slice Domestic Flights\n"
      "5. Exit\n")
while True:
    option = int(input("Enter the option : "))
    if option == 1:
        view(flight_numbers)
    elif option == 2:
        search(flight_numbers)
    elif option == 3:
        total(flight_numbers)
    elif option == 4:
        sliceing(flight_numbers)
    elif option == 5:
        break
    else:
        print("invalid option !")


