# Requirements:

# Take student name.
# Take 5 subject marks.
# Create functions:
# calculate_total()
# calculate_percentage()
# calculate_grade()
# generate_report()
# Return values from each function.
# Display a complete report.

# Example:

# ------ Student Report ------

# Name: Akshata

# Total Marks: 450
# Percentage: 90%

# Grade: A

# Status: Pass
# ----------------------------

def calculate_total(marks_1,marks_2,marks_3,marks_4,marks_5,total_mark_of_exam):
    total_marks = sum(marks)
    return total_marks


def calculate_percentage(*marks,total_mark_of_exam):
    total_percentage = (calculate_total(marks_1,marks_2,marks_3,marks_4,marks_5,total_mark_of_exam)/total_mark_of_exam )*100
    return total_percentage


def calculate_grade(marks_1,marks_2,marks_3,marks_4,marks_5):
    pass

def generate_report(marks_1,marks_2,marks_3,marks_4,marks_5):
    pass
name = input("Enter your name : ")
marks_1 = int(input ("Enter marks 1 :"))
marks_2 = int(input ("Enter marks 2 :"))
marks_3 = int(input ("Enter marks 3 :"))
marks_4 = int(input ("Enter marks 4 :"))
marks_5 = int(input ("Enter marks 5 :"))
total_mark_of_exam = float(input("Enter the total marks of the exam :"))

final_marks = calculate_total(marks_1,marks_2,marks_3,marks_4,marks_5,total_mark_of_exam)
print(final_marks)

final_percentage = calculate_total(marks_1,marks_2,marks_3,marks_4,marks_5,total_mark_of_exam)
print(final_percentage)