# guessing number
b=10
while True:
    num = int(input("Enter the number that you guessed :"))
    if b==num :
        print("CONGRACULATION")
        break
    else:
        print("try again")