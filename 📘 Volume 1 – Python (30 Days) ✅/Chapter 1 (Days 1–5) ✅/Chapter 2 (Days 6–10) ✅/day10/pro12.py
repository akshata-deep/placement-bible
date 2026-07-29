# 4. Student Marks

# Take input for:

# Student Name
# Python Marks
# Java Marks
# SQL Marks

# Calculate:

# Total
# Average


student_name = input("Enter the name of the student :")
python_marks = int(input("Enter the python marks :"))
java_marks = int(input("Enter the java marks :"))
sql_marks = int(input("Enter the sgl marks :"))

total = python_marks + java_marks + sql_marks
average = (python_marks + java_marks + sql_marks)/3


print(f"========= STUDENT RESULT ==========\n"
      f"NAME : {student_name}\n"
      f"PYTHON MARKS : {python_marks}\n"
      f"JAVA MARKS : {java_marks}\n"
      f"SQL MARKS : {sql_marks}\n"
      f"TOTAL MARKS: {total}\n"
      f"AVERAGE : {average}\n"
      f"===================================")