# # ===== STUDENT RESULT =====

# # Enter Name : Akshata
# # Enter Roll No : 21

# # English : 95
# # Maths : 90
# # Science : 92

# # ------------------------
# # Name : Akshata
# # Roll No : 21

# # Total : 277
# # Average : 92.33

# # Grade : A

# # Result : PASS



def student_details():
    name = input("Enter name :")
    roll_number = input("Enter roll number :")
    return name,roll_number


def marks():
    english = int(input("Enter the marks of english :"))
    maths = int(input("Enter the marks of maths : "))
    science = int(input("Enter the marks of science : "))
    return english,maths,science

def result(english,maths,science):
    total = english + maths + science
    average = total/3
    print(f"\nTotal : {total}\n"
          f"Average : {average}\n")
    return total,average

def grade():
    total = english + maths +science
    if total >= 90:
        print("Grade A!")
    elif total >= 75:
        print("Grade B!")
    elif total >= 50:
        print("Grade C!")
    elif total >= 49:
        print("Fail!")
    else:
        print("invalid !")

def final_result():
    total = english + maths + science
    if total <=49:
        print("Result : Fail")
    else :
        print("Result : PASS")






print(f"===== STUDENT RESULT =====\n")
name,roll_number = student_details()
english,maths,science = marks()
print("-------------------------------------")
print(f"Name: {name}\n"
      f"roll number : {roll_number}\n")
result(english,maths,science)

grade()
final_result()

