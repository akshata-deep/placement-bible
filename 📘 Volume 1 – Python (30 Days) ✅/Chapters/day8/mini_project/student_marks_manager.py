def all_marks():
    print("MARKS :")
    for i in range(0,len(marks)):
        print(marks[i])


def add_marks():
    new = int(input("enter the new marks :"))
    marks.append(new)
    print("Mark added successfully!")

def remove_marks():
    new = int(input("Enter the marks :"))
    if new in marks:
        marks.remove(new)
        print("Mark removed successfully!")
    else:
        print("this marks is not in list! ")

def max_marks():
    print(f"hightest marks is :{max(marks)}")

def average_marks():
    average = (sum(marks)/len(marks))
    print(f"AVERAGE MARKS : {average:.2f}")





marks = [75, 80, 65, 90, 88]

while True:
    print("\n----- Student Marks Manager -----")
    print("1. Display Marks")
    print("2. Add Mark")
    print("3. Remove Mark")
    print("4. Highest Mark")
    print("5. Average Marks")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        all_marks()
    elif choice == 2:
        add_marks()
    elif choice == 3:
        remove_marks()
    elif choice == 4:
        max_marks()
    elif choice == 5:
        average_marks()
    elif choice == 6:
        print("Thank you!")
        break
    else:
        print("invalid option!")




