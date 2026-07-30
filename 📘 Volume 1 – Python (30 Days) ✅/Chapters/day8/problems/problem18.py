# Write a program to print the largest mark.

marks = [75, 80, 100, 90, 88]
largest = marks[0]
for mark in marks:
    if mark > largest :
        largest = mark
print(largest)