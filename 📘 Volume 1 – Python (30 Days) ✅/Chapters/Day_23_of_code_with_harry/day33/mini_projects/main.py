





students = {}


print("===== Student Marks Manager =====\n"
      "1. Add Student\n"
      "2. Search Student\n"
      "3. Display All Students\n"
      "4. Display All Marks\n"
      "5. Exit\n")
while True:
    option = int(input("Enter the option :"))
    if option == 1:
        name = input("Enter the name : ")
        marks = int(input("Enter the marks : "))
        students[name] = marks
        print("Name and Marks are successfully added")
    elif option == 2:
        name = input("Enter the name : ")
        print(f"The marks of {name} is {students[name]}")
    elif option == 3:
        print(f"All the students names : {students.keys()}")
    elif option == 4:
        print(f"All the students marks : {students.values()}")
    elif option == 5:
        break
    else:
        print("invalid option !")


