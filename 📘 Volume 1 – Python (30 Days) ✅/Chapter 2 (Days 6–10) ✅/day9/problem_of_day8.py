def all_students(students):
    for student in students:
        print(student)

def find_students(students):
    name = (input("Enter the name :"))
    for student in students:
        if student[0] == name :
            print(f"{student[0]} scroed {student[1]}")
            break
    
    else: 
        print("this name is not in list")

def add_student(students):
    name = input("Enter the name :")
    marks = int(input("Enter the marks :"))
    students.append([name,marks])
    print("YOUR NAME AND MARKS ARE ADDED !")


def remove_student(students):
    print("\nWhat do you want to remove?")
    print("1. Remove only Marks")
    print("2. Remove only Name")
    print("3. Remove Entire Student")

    option = int(input("Enter your option: "))

    if option == 1:
        marks = int(input("Enter the marks: "))

        for student in students:
            if len(student) > 1 and student[1] == marks:
                student.remove(marks)
                print("Marks removed successfully!")
                break
        else:
            print("Marks not found!")


    elif option == 2:
        name = input("Enter the name: ")

        for student in students:
            if len(student) > 0 and student[0] == name:
                student.remove(name)
                print("Name removed successfully!")
                break
        else:
            print("Name not found!")


    elif option == 3:
        name = input("Enter the student name: ")

        for student in students:
            if student[0] == name:
                students.remove(student)
                print("Student removed successfully!")
                break
        else:
            print("Student not found!")

    else:
        print("Invalid option!")
    

def highest_mark(students):
    largest = 0
    for stdents in students:
        if stdents[1]>largest:
            largest = stdents[1]
    print(f"the largest marks is :{largest}")

def average_marks(students):
    sum = 0
    for student in students:
        sum += student[1] 
        average = sum/len(students)
    print(average)
            
                
            


        
        




students = [
    ["Harry", 85],
    ["Sarah", 92],
    ["Bruno", 78],
    ["Akshata", 95],
    ["Rahul", 85]
]
while True:
    option = int(input("Enter the option :"))
    if option == 1:
        all_students(students)
    elif option == 2:
        find_students(students)
    elif option == 3:
        add_student(students)
    elif option == 4:
        remove_student(students)
    elif option == 5:
        highest_mark(students)
    elif option == 6:
        average_marks(students)
    elif option == 7:
        print("Thankyou !")
        break
   
    else :
        print("invalid option!")