# Ask the user to enter a mark to remove.
# Remove that mark from the list.
# Print the updated list.


marks = [75, 80, 65, 90]
mark = int(input("Enter the mark which you wnat to delete :"))
if mark in marks:
    marks.remove(mark)
    print(marks)
else:
    print("this number is not in list")