# Print "Topper!" when marks are >= 90, along with the student's index.


marks = [85, 92, 78, 90, 88]
for index,mark in enumerate(marks):
    if mark >= 90:
        print(f"Topper!\n{mark} index is {index}")