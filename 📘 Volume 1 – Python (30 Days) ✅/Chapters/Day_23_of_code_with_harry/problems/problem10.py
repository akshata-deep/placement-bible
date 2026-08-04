students = {
    "Akshata": 85,
    "Anu": 92,
    "Rahul": 78,
    "Amruta": 90
}


print(students.keys())
print(students.values())
name = input("Enter the name of the student : ")
print(students.get(name))