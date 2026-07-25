# Largest of Two Numbers

# Write a program that:

# Takes two integers as input.
# Prints:
# "First number is larger" if the first number is greater.
# "Second number is larger" if the second number is greater.
# "Both numbers are equal" if both are equal.


num1 = input("Enter the number 1 :")
num2 = input("Enter the number 2 :")
if num1 > num2 :
    print (f"{num1} is greater")
elif num2 > num1 :
    print (f"{num2} is greater")
else :
    print (f"{num1} and {num2}are equle")

