# Question 5 — Moderate 🏢 (Accenture Style)
# 📌 Problem: Student Percentage

# Create a function that:

# Accepts marks of English, Maths, and Science.
# Returns the percentage.
# Print the percentage in the main program.


def percentage():
    english = int(input("Enter the marks of english : "))
    maths = int(input("Enter the marks of maths : "))
    science = int(input("Enter the marks of science : "))
    marks_percentage = ((english + maths + science)/300)*100
    return marks_percentage


marks_percentage = percentage()
print(f"the percentage of marks is : {marks_percentage}%")