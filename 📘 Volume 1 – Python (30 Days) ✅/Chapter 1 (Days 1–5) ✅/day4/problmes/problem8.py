# sum of  N

num = int(input("give me the number :"))
sum = 0
if num == 0 :
    print("the sum of 0 is 0 itself")
else :
    for i in range (1, num + 1):
        sum = sum + i                       
    print(f"the sum of {num} is : {sum}")         