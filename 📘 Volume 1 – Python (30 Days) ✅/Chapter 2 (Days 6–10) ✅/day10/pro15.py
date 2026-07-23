# Take input for:

# Student Name
# USN
# Marks in 5 subjects

# Calculate:

# Total
# Average
# Percentage (same as average, assuming each subject is out of 100)


name = input("Enter the name of the student :")
usn = input("Enter the usn :")
marks1 = int(input("Enter the marks of 1th subject :")) 
marks2 = int(input("Enter the marks of 2th subject :")) 
marks3 = int(input("Enter the marks of 3th subject :")) 
marks4 = int(input("Enter the marks of 4th subject :")) 
marks5 = int(input("Enter the marks of 5th subject :")) 

total = marks1 + marks2 + marks3 + marks4 + marks5
average = total/5
percentage = (total/500)*100

print(f"============ RESULT ============\n"
      f"NAME : {name}\n"
      f"USN : {usn}\n"
      f"TOTAL : {total}\n"
      f"AVERAGE : {average}\n"
      f"PERCENTAGE : {average}\n"
      f"==========================")