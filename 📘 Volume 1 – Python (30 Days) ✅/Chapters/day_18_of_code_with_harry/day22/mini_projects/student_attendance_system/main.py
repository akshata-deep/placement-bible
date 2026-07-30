# Beginner Mini Project
# 📌 Project: Student Attendance System
# Objective

# Create a simple attendance management program using lists.

# Requirements
# Create a list containing at least 8 student names.
# Display all student names with serial numbers.
# Ask the user to enter a student's name.
# Check whether the student is present in the list.


name = ["Akshata","Rahul","Sneha","Priya","Kiran","Ravi","Anjali","Mohan"]
print("========== Student Attendance System ==========\n")
serial_number = 0
for i in name:
    serial_number += 1
    print(f"{serial_number}.{i}")

search_name = input("\nEnter the name : ")
if search_name in name:
    print("\nAttendance Recorded")
else:
    print("\nStudent Not Found")
