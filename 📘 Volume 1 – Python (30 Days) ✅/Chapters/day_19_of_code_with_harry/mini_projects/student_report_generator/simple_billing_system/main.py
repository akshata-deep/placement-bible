name  = input("Enter the name: ")
roll_number = input("Enter the Roll number: ")
python_marks = int(input("Enter the Python marks: "))
das_marks = int(input("Enter the DSA marks: "))
sql_marks = int(input("Enter the SQL marks : "))
total = python_marks + das_marks +sql_marks
average = total/3
print(f"============ Student Report Generator ===============\n"
      f"Name : {name}\n"
      f"Roll number : {roll_number}\n"
      f"Python marks : {python_marks}\n"
      f"DSA marks : {das_marks}\n"
      f"SQL marks : {sql_marks}\n"
      "-----------------------------\n"
      f"Total : {total}\n"
      f"Average : {average:.2f}\n")