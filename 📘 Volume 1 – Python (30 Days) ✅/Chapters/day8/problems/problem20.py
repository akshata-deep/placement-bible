# Write a program that:

# Asks the user to enter a mark.
# If the mark exists in the list, print:


marks = [75, 80, 65, 90, 88]
mark = int(input("Enter the mark :"))
if mark in marks:
    print("MARK FOUND!....")
else:
    print("MARK NOT FOUND!...")