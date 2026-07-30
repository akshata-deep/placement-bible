def name():
    name = input("Enter the name:")
    return name

def marks():
    english = int(input("Enter the english marks :"))
    maths = int(input("Enter the maths marks :"))
    science = int(input("Enter the science marks :"))
    return english,maths,science

# def total(english,maths,science):
#     total = english + maths + science
#     return total

# def average(total):
#     average = total/3
#     return average

# def grade(average):
#     if average >=90:
#         grade = "A"
#     elif average >=80:
#         grade= "B"
#     elif average >=70:
#         grade="C"
#     elif average >=60:
#         grade="Fail"
#     else:
#         grade="invalid"
#     return grade

# def result(grade):
#     if grade == "A" or "B" or "C":
#         result = "pass"
#     else:
#         result = "fail"
#     return result

def result(name,english,maths,science):
    total = english + maths +science
    average = total/3

    if average >=90:
        grade = "A"
    elif average >=80:
        grade = "B"
    elif average >=70:
        grade = "C"
    elif average >=60:
        grade = "D"
    else:
        grade = "Fail"

    if average >=90:
        result = "PASS"
    elif average >=80:
        result = "PASS"
    elif average >=70:
        result = "PASS"
    elif average >=60:
        result = "PASS"
    else:
        result = "Fail"


    print(f"=========== Student Result ============\n"
          f"Name : {name}\n\n"
          f"English : {english}\n"
          f"Maths : {maths}\n"
          f"Science : {science}\n\n"
          f"Total : {total}\n"
          f"Average : {average}\n"
          f"Grade : {grade}\n"
          f"Result : {result}")






name = name()
english,maths,science = marks()
result(name,english,maths,science)
