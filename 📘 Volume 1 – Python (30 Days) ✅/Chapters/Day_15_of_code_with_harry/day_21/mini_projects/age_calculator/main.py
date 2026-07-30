# 📌 Project: Age Calculator Using Functions
# Objective

# Create a program that calculates a person's age.

# Requirements

# Create separate functions for:

# Get the user's name.
# Get the birth year.
# Calculate the age.
# Display the final result.
# Sample Output
# ========== AGE CALCULATOR ==========

# Enter Name : Akshata
# Enter Birth Year : 2005

# ----------------------------

# Name : Akshata
# Birth Year : 2005
# Age : 21 years

# 💡 Assume the current year is 2026.



def user_name():
    name = input(f"========== AGE CALCULATOR ==========\n\n"
                 f"Enter the name       : ")
    return name

def birth_year():
    b_year = int(input("Enter the birth year : "))
    print("----------------------------")
    return b_year

def calculate_age(b_year):
    current_year = 2026
    age = current_year - b_year
    return age

def result(name,b_year,age):
    print(f"NAME       : {name}\n"
          f"BIRTH YEAR : {b_year}\n"
          f"AGE        : {age} years\n")


name = user_name()
b_year = birth_year()
age = calculate_age(b_year)
result(name,b_year,age)