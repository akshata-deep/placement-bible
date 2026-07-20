# Student Result Analyzer (Improved)

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


def calculate_total(*marks):
    total_marks = sum(marks)
    return total_marks


def calculate_percentage(*marks):
    total_percentage = ((sum(marks))/total_mark_of_exam )*100
    return total_percentage


def calculate_grade(*marks):
    percentage = calculate_percentage(*marks)
    if 91 <= percentage <= 100:
        a = "\'A\'"
        return a
    elif 81 <= percentage <= 90:
        b = "\'B\'"
        return b
    elif 71 <= percentage <= 80:
        c = "\'C\'"
        return c
    elif 61 <= percentage <= 70:
        d = "\'D\'"
        return d
    elif 41 <= percentage <= 60:
        e = "\'E\'"
        return e
    elif 0 <= percentage <= 40:
        f = "\'F\'"
        return f
    else:
        g = "invalid !...."
        return g

def do_stauts(*marks):
    percentage = calculate_percentage(*marks)
    if 91 <= percentage <= 100:
        a = "pass"
        return a
    elif 81 <= percentage <= 90:
        b = "pass"
        return b
    elif 71 <= percentage <= 80:
        c = "pass"
        return c
    elif 61 <= percentage <= 70:
        d = "pass"
        return d
    elif 41 <= percentage <= 60:
        e = "pass"
        return e
    elif  0 <= percentage <= 40:
        f = "fail"
        return f
    else:
        g = "invalid !...."
        return g
    

def generate_report(name,final_marks,final_percentage,final_grade,final_stauts):
    print ("-------------------------- Student Report --------------------------\n"
           f"Name: {name}\n"
           f"Total Marks: {final_marks}\n"
           f"Percentage: {final_percentage}%\n"
           f"Grade: {final_grade}\n"
           f"Status: {final_stauts}\n"
           "--------------------------------------------------------------------")

name = input("Enter your name : ")
marks_1 = int(input ("Enter marks 1 :"))
marks_2 = int(input ("Enter marks 2 :"))
marks_3 = int(input ("Enter marks 3 :"))
marks_4 = int(input ("Enter marks 4 :"))
marks_5 = int(input ("Enter marks 5 :"))
total_mark_of_exam = float(input("Enter the total marks of the exam :"))

final_marks = calculate_total(marks_1,marks_2,marks_3,marks_4,marks_5,)
final_percentage = calculate_percentage(marks_1,marks_2,marks_3,marks_4,marks_5)
final_grade = calculate_grade(marks_1,marks_2,marks_3,marks_4,marks_5)
final_stauts  = do_stauts(marks_1,marks_2,marks_3,marks_4,marks_5)
generate_report(name,final_marks,final_percentage,final_grade,final_stauts)