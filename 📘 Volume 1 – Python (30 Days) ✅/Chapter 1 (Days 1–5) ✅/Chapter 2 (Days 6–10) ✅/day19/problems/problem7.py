# Search for a number in a list.


asked_number = int(input("Enter the number :"))

numbers = [12, 25, 40, 55, 70]
for num in numbers:
    if asked_number in numbers:
        print("Number Found")
        break
else:
    print("Number Not Found")


    # Run the else block only if the loop finished normally (without hitting break).