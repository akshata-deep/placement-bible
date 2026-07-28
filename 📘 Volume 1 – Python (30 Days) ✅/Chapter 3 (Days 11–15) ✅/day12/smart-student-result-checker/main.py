student_name = input("Enter Student Name: ")
usn = input("Enter USN: ")
marks = int(input("Enter Marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "Fail"

if marks >= 40:
    result = "PASS"
else:
    result = "FAIL"

print("\n========== STUDENT REPORT ==========")
print(f"Name   : {student_name}")
print(f"USN    : {usn}")
print(f"Marks  : {marks}")
print(f"Grade  : {grade}")
print(f"Result : {result}")
print("====================================")