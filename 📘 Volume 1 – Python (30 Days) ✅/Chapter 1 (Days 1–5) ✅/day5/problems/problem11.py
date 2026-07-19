# rivers number

num = int(input("Enter the number :"))
a=0
for i in range (1,num+1):
    if i != num:
        a = num-i
        print(a)