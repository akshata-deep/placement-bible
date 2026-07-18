# write a program to find sum of first n natural numbers using while loop
num = int(input("Enter the number it u you what to add :"))
sum = 0
for i in range (0,num+1):
    sum = sum + i
print(f"your answer is :{sum}")