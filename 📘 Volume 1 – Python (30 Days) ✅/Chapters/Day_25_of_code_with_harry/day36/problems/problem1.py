# Q1 — Basic Try-Except

# Write a program that asks the user for an integer and handles invalid input.


try:
    num = int(input("Enter the number : "))
    print(num)
except Exception as e:
    print(e)