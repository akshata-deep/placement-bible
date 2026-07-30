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
    percentage = calculate_total(*marks)
    if 100<= percentage <=91:
        a = "GRADE : \'A\'"
        retuen a
    elif 90<= percentage <=81:
        b = "GRADE : \'B\'"
        retuen b
    elif 80<= percentage <=71:
        c = "GRADE : \'C\'"
        retuen c
    elif 70<= percentage <=61:
        d = "GRADE : \'D\'"
        retuen d
    elif 40<= percentage <=51:
        e = "GRADE : \'E\'"
        retuen e
    else: #0<= percentage <=41:
        f = "GRADE : \'F\'"
        retuen f
    # else:
    #     print("invalid !....")

def do_stauts(*marks):
    percentage = calculate_total(*marks)
    if 100<= percentage <=91:
        a = "pass"
        retuen a
    elif 90<= percentage <=81:
        b = "pass"
        retuen b
    elif 80<= percentage <=71:
        c = "pass"
        retuen c
    elif 70<= percentage <=61:
        d = "pass"
        retuen d
    elif 40<= percentage <=51:
        e = "pass"
        retuen e
    else : #0<= percentage <=41:
        f = "fail"
        retuen f
    # else:
    #     print("invalid !....")
    

def generate_report(name,final_marks,final_percentage,final_grade,final_stauts):
    print ("-------------------------- Student Report --------------------------\n"
           f" Name: {name}\n"
           f"Total Marks: {final_marks}\n"
           f"Percentage: {final_percentage}\n"
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
generate_report(generate_report(name,final_marks,final_percentage,final_grade,final_stauts))