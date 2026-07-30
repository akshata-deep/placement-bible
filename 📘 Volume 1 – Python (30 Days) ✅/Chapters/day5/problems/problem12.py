# menu program

while True:
    print("1.GUESSING GAME:")
    print("2.MULTIPICATION TABLE :")
    print("3.PALANDROM PROGRAM :")
    print("4.LOOP PROGRAM:")
    print("5.EXIT:")

    choice = int(input("Enter the your choices : "))

    if choice == 1:
        print(" basically we hided the number in program the user need to guess that \n \"simple right\" ")
    if choice == 2:
        print(" here the number will be take from the users and print that particular number mutiplication table \n \"simple right\" ")
    elif choice == 3:
        print("In this program the number of rows will be take as a input and then according to that row that palandrom of the stars will be generate \n \"simple right\" ")
    elif choice == 4:
        print("The looping we use basicly for to print the values repit. \n \"simple right\" ")
    elif choice == 5:
        print(" This menu ends here \'  THANKYOU FOR REACHING OUT \' ")
        break
    else :
        print("invalid choices")
    