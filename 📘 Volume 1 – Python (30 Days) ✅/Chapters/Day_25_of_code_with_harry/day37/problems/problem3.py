# Create a multiplication table program using try, except, and finally.

try :
    num = int(input("Enter the number : "))
    for i in range (1,11):
        print(f"{num} X {i} = {num*i}")
except:
    print("Value Error")
finally:
    print("Are you ready for other multiplication table")