# Beginner Mini Project × 1

# Project Name: Student Profile Card

# Objective:
# Practice string slicing, indexing, len(), and input().

# Requirements:

# Take input:

# Student Name
# USN
# Branch
# College

# Print:

# Student Details
# First Character of Name
# Last 4 Characters of College
# First 3 Characters of Branch
# Length of Student Name

student_name = input("Enter the name :")
usn = input("Enter the USN :")
branch = input("Enter the brnach :")
college = input("Enter the college name :")

print(f"================== STUDENT DETAILS ===============\n"
      f"NAME : {student_name}\n"
      f"USN : {usn}\n"
      f"BRANCH : {branch}\n"
      f"COLLAGA : {college}\n\n"
      f"First Character of Name : {student_name[0]}\n"
      f"Last 4 Characters of College : {college[-4:]}\n"
      f"First 3 Characters of Branch : {branch[:3]}\n"
      f"Length of Student Name : {len(student_name)}\n"
      f"===================================================")