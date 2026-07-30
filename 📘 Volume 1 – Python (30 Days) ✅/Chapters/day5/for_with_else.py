

num = int(input("Enter the number :"))
a = 0
for i in range(0,(num*10)+1,num) :
    if i == 0 :
        print()
    else:
        a+=1
        print(f"{num} X {a} = {i} ")


# when we will use tis else means when the lopp will compelete its work then it will go to else a do its work
else :
    print ("DONE")