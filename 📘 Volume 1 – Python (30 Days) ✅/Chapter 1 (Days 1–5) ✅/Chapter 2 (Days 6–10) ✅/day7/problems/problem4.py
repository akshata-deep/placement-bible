# 4. Student Marks Analyzer
# Use *args.
# Input multiple marks.
# Return:
# total marks
# average marks
# highest mark

def analyzer(*marks):
    total = sum(marks)
    average = total/len(marks)
    highest = max(marks)
    return total,average,highest

print("                 WELCOME TO STUDENT MARKS ANALYZER\n"
      "-----------------------------------------------------------------")
marks_1 = int(input("enter the marks 1:"))
marks_2 = int(input("enter the marks 2:"))
marks_3 = int(input("enter the marks 3:"))
marks_4 = int(input("enter the marks 4:"))
marks_5 = int(input("enter the marks 5:"))
marks_6 = int(input("enter the marks 6:"))
total_marks = analyzer(marks_1,marks_2,marks_3,marks_4,marks_5,marks_6)
print(f"your sum of the marks are :{total_marks[0]}\n"
      f"your average mark is :{total_marks[1]}\n"
      f"your hightest marks is :{total_marks[2]}\n"
      "-----------------------------------------------------------------")