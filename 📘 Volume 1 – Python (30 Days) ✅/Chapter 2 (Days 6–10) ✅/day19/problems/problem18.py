numbers = [10, 20, 30, 40, 50]
user_number = int(input("Enter the number : "))
for num in numbers:
    if num == user_number:
        print("Number Found")
        break
else:
    print("Number Not Found")
