# Question 5 — Placement Level ⭐⭐⭐⭐

# Create a menu-driven Student List Manager.

# ===== MENU =====
# 1. View Students
# 2. Add Student
# 3. Remove Student
# 4. Search Student
# 5. Exit

# Requirements:

# Use functions.
# Use append().
# Use remove().
# Use in.
# Continue until Exit.

def view_students(students):
    print(students)


def add_student(students):
    new_student = input("Enter the student name : ")
    if new_student in students:
        print("this students name is already in the list do you want to add again\n"
              "1.YES\n"
              "2.NO\n")
        option = int(input("Enter the option : "))
        if option == 1:
            students.append(new_student)
            print("New Student is added in list")
        elif option == 2:
            print("Ok !")
    else:
        students.append(new_student)
        print("New Student is added in list")

def remove_student(students):
    new_name = input("Enter the name : ")
    if new_name in students:
        students.remove(new_name)
        print("Name removed !")
    else:
        print("This name is not in the list !")

    

def search_student(students):
    new_student = input("Enter the name : ")
    if new_student in students:
        print(f"Yes this name is present in list {students.count(new_student)} time")
    else:
        print("This name is not in list")






students = ["Akshata","Amruta","Santhosh","Prema","Shantaveer"]
print("===== MENU =====\n"
      "1. View Students\n"
      "2. Add Student\n"
      "3. Remove Student\n"
      "4. Search Student\n"
      "5. Exit\n")
while True:
    option = int(input("Enter the option : "))
    if option == 1:
        view_students(students)
    elif option == 2:
        add_student(students)
    elif option == 3:
        remove_student(students)
    elif option == 4:
        search_student(students)
    elif option == 5:
        break
    else:
        print("invalid option !")