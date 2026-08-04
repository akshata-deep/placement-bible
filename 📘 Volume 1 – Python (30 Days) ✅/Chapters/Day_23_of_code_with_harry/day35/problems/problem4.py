numbers = [10, 20, 30, 40, 50]
give_me = int(input("Enter the number: "))
while True:
    i = 0
    if numbers[i] == give_me:
        print("Number found")
        break
    i+=1
else:
    print("Number not found")