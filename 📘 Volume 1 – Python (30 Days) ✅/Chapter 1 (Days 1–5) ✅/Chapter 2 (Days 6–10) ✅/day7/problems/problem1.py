# # 1. Student Information Function

# Create a function that accepts:

# name
# age
# course

# Use keyword arguments while calling.

def details(s_name,s_age,s_course):
    print(f"---------- STUDENT INFORMATION ---------\n"
          f"NAME : {s_name}\n"
          f"AGE : {s_age}\n"
          f"COURSE : {s_course}\n"
          "------------------------------------------")

name = input("Enter the name :")
age = input("Enter the age :")
course = input("Enter the course :")
details(s_name=name,s_age=age,s_course=course)
# info(s_name,s_age,s_course)