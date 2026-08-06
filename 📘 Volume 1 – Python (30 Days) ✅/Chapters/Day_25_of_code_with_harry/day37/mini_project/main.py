try:
    marks = int(input("Enter the student marks:"))
    percentage = (marks/100)*100
    print(percentage)

except:
    print("Error")
finally:
    print("Thank you for using Student Result Viewer.")
