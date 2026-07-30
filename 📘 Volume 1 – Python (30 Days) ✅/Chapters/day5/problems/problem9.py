row = int(input("Enter a number:"))
for i in range(1,row+1):
    if i >1 and i<= row-1:
        print("*","  "*(row-2),"*")
    else:
        print("* "*row)