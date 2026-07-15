# Scientific Calculator

# Hints:
# 1. Take two numbers as input.
# 2. Ask the user to choose +, -, *, /.
# 3. Use if-elif to perform the operation.
# # 4. Display the result.

num1 = float(input("Enter the number 1 :"))
num2 = float(input("Enter the number 2 :"))
a = 0

Addition = num1 + num2
subtartion = num1 - num2
divition = num1 / num2
multiplication = num1 * num2 

Input = int(input(" addition press 1 \n subtartion press 2 \n divition press 3 \n multipication press 4 \n"))

b = float(a)

if Input == 1:
    b = num1 + num2
    print("answer is :", b)
elif Input == 2:
    b = num1 - num2 
    print("answer is :" ,b)
elif Input == 3:
    b = num1 / num2 
    print("answer is :", b)
elif Input == 4:
    b = num1 * num2 
    print("answer is :" ,b)