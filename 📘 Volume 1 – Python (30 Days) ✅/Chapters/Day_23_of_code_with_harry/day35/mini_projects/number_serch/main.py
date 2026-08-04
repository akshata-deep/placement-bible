numbers = [10, 20, 30, 40, 50, 60, 70]
print("===== Number Search =====")
num = int(input("Enter a number to search : "))
for i in numbers:
    if i == num:
        print("Number found!")
        break
else:
    print("Number not found!")