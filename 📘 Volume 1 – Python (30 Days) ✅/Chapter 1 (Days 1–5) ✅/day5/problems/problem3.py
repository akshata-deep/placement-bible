# write a program to print multiplication table of a given number using for loop

num = int(input("Enter the number:"))
i = 0
while i<= 9:
    i += 1
    sum = num * i
    print(f"{num} X {i} = {sum}") 
