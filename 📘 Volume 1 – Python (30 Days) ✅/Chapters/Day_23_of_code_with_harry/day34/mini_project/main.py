employee = {
    122: 45,
    123: 89,
    567: 69
}

print("===== Employee Performance Manager =====\n"
      "1. Add Employee\n"
      "2. Update Performance\n"
"3. Remove Employee\n"
"4. Remove Last Employee\n"
"5. Display All Employees\n"
"6. Clear All Employees\n"
"7. Exit")

while True :
    option = int(input("Enter the option : "))
    if option == 1:
        id = int(input("Enter the employee id : "))
        if id in employee:
            print("This id is already precent!")
        else:
            performances = int(input("Enter the employee performances :"))
            employee[id]=[performances]
            print("This employee infomation is added!")

    elif option == 2:
        id = int(input("Enter the employee id : "))
        if id in employee:
            performances = int(input("Enter the employee performances :"))
            employee.update({id:performances})
            print("performance is updated!.")
        else:
            print("This id is not in the dictionary! ")
    elif option == 3:
        id = int(input("Enter the id : "))
        if id in employee:
            del employee[id]
            print("This employee id and performances is removed!")
        else:
            print("This id is not in the dictionary !")    
    elif option == 4:
        employee.popitem()
        print("The last id and performances is removed!") 
    elif option == 5:
        print(employee.keys())
    elif option == 6:
        employee.clear()
        print("Now the employee dictionary is empty!")
    elif option == 7:
        break
    else:
        print("invalid option!")   