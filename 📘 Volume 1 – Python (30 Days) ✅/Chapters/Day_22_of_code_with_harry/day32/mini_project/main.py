











students_python = {"Akshata", "Anu", "Rahul", "Amruta"}
students_sql = {"Akshata", "Rahul", "Kiran", "Sneha"}


print("===== Course Enrollment Analyzer =====")
print(f"1. All students")
print(f"2. Students in both courses")
print(f"3. Only Python students")
print(f"4. Only SQL students")
print(f"5. Students in exactly one course")
print(f"6. Check whether courses have no common students")
print("7. Exit")


while True:
    option = int(input("Enter the option : "))
    if option == 1:
        print(students_python.union(students_sql))
    elif option == 2:
        print(students_python.intersection(students_sql))
    elif option == 3:
        print(students_python)
    elif option == 4:
        print(students_sql)
    elif option == 5:
        print(students_sql.symmetric_difference(students_python))
    elif option == 6:
        print(students_sql.isdisjoint(students_python))
    elif option == 7:
        break
    else:
        print("invalid option !")

    
    