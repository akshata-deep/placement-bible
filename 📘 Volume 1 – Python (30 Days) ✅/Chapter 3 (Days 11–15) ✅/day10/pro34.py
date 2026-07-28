# Program 10 – ID Card

# Take input:

# Name
# USN
# Branch
# College

# Print a neat ID card and also print:

# First letter of the name
# Last 3 letters of the college name
# # Length of the branch


name = input("Enter the name :")
usn = input("Enter the USN :")
branch =  input("Enter the branch :")
college = input("Enter the college :")

print(f"========== ID CARD ==========\n"
      f"NAME : {name}\n"
      f"USN : {usn}\n"
      f"BRANCH : {branch}\n"
      f"COLLEGE : {college}\n\n"
      f"First letter of the name : {name[0]}\n"
      f"Last 3 letters of the college name : {college[-3:]}\n"
      f"length of the branch : {len(branch)}\n"
      f"================================")