# Create a Student Marks Viewer using enumerate() that displays student names and marks together.


print("=============== STUDENT MARKS VIEWER ===============")
names = ["Alex", "Ben", "Charlie", "Daisy", "Ethan"]
marks = [85, 92, 78, 90, 88]

for name,mark in zip(names,marks):
        print(f"{name} : {mark}")