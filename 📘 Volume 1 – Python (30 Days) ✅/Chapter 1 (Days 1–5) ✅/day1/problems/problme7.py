# Swap numbers


# method 1
num1 = 22
num2 = 33
print("number is swaped")

a = num1
num1 = num2
num2 = a
print(num1,num2)


# method 2 

num1 = 22
num2 = 33
print(f"before {num1} {num2}")

num1,num2 = num2,num1

print(f"after {num1} {num2}")

