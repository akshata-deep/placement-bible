# # Student Grade System

# Hints:
# 1. Ask for student name and marks.
# 2. Use if-elif-else to assign a grade.
# 90–100  → Grade A
# 80–89   → Grade B
# 70–79   → Grade C
# 60–69   → Grade D
# 50–59   → Grade E
# Below 50 → Fail
# # 3. Display name, marks and grade.


name = input("enter your name :")
marks = int(input("Enter the marks :"))
if 90 <= marks <= 100 :
    a="Grade A !"
elif 80 <= marks <= 89 :
    a= "Grade B !"
elif 70 <= marks <= 79 :
    a= "Grade C !"
elif 60 <= marks <= 69 :
    a= "Grade E !"
elif marks <= 50 :
    a= "Grade F !"
print (f"Hello {name} \nyour marks is : {marks} \nThe grade is : {a}")