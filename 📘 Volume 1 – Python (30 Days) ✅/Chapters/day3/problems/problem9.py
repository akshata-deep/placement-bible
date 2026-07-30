# 5. Electricity Bill

units = int(input("Enter the units you used :"))
if 0< units <=100 :
    bill = units * 10 
    print(f"your bill is : {bill}")
elif 100< units <=200 :
    bill = units * 7 
    print(f"your bill is : {bill}")
elif 300< units <=400 :
    bill = units * 5 
    print(f"your bill is : {bill}")
elif 400 < units :
    bill = units * 2
    print(f"your bill is : {bill}")
else :
    print("your bill is 0")