# Personal_expense_calculator
# Hints:
# 1. Take daily expenses.
# 2. Create add_expense() function.
# 3. Calculate total expense.
# # 4. Print summary.

# output :------ Expense Summary ------
# Bus    : 100
# Food   : 200
# Books  : 300
# Tuition: 150
# Pen    : 100
# -----------------------------
# Total  : 850


def add_expense(bus,food,books,tution,pen):
    total = bus+food+books+tution+pen
    return total

bus = int(input("Enter the amount you gave for bus:"))
food = int(input("Enter the amount you gave for food:"))
books = int(input("Enter the amount you gave for books:"))
tution = int(input("Enter the amount you gave for tution:"))
pen = int(input("Enter the amount you gave for pen:"))

# print(f"------ Expense Summary ------\n Bus    : {bus} \n Food   : {food} \n Books  : {bus} \n Tuition: {tution} \n Pen    : {pen} \n ----------------------------- \n Total  : ",add_expense(bus,food,books,tution,pen))

# dont do like this becouse you only one will not read the program in company so

print(f"------ Expense Summary ------\n"
    f"Bus    : {bus}\n"
    f"Food   : {food}\n"
    f"Books  : {bus}\n" 
    f"Tuition: {tution}\n"
    f"Pen    : {pen}\n"
    f"-----------------------------\n"
    f"Total  : ",add_expense(bus,food,books,tution,pen))