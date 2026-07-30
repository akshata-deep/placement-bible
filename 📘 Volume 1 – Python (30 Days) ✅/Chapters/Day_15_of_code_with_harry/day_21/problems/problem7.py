# Question 7 — High 🏢 (IBM Style)
# 📌 Problem: Employee Salary Calculator

# Create a function that:

# Accepts:
# Employee Name
# Basic Salary
# Calculates:
# HRA = 20%
# DA = 10%
# Total Salary = Basic + HRA + DA
# Return all calculated values.
# Print a formatted salary report


def emoloyee_information():
    name = input("Enter the name : ")
    salary = int(input("Enter the salary : "))
    hrd = salary * (20/100)
    da = salary * (10/100)
    total_salary = salary + hrd + da
    return name,salary,total_salary




name,salary,total_salary = emoloyee_information()
print(f"=============== salary report ==============\n"
      f"Employee Name : {name}\n"
      f"Basic salary  : {salary}\n\n"
      f"Total Salary  : {total_salary}\n"
        "Note : HRD = 20%  & DA = 10%")
