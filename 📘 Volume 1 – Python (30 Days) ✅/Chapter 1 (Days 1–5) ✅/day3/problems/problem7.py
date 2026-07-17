name = input("Enter your name :")
age = int(input("Enter your age :"))

if age>18 :
    print("you are avaliad to do the volting :")
else :
    age = 18 - age
    if age == 1:
        print(f"just wait for {age} year ")
    else :
        print(f"just wait for {age} year\'s ")

