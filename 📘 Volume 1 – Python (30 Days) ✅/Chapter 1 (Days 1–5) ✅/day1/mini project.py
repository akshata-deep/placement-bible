# Student Information System

# # Hints:
# 1. Ask the user to enter Name, Age and USN.
# 2. Store the values in variables.
# 3. Print the details in a neat format.
# 4. (Optional) Ask for marks and calculate total.


name = input("enter the name:")
age = int(input("enter the age:"))
usn = input("enter the usn:")
marks1=int(input("enter the marks1:"))
marks2=int(input("enter the marks2:"))
marks3=int(input("enter the marks3:"))

total_marks = marks1 + marks2 + marks3

print(f"your name is :{name} \n your age is : {age} \n your usn is : {usn} \n your total marks is : {total_marks}")