# factorial using for loop

num = int(input("Enter the number of factorical :"))
sum = 1
for i in range (1,num+1):
    sum = sum * i
print(f"your answer is {sum}")