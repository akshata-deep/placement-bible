def add(a,b):
    print(f"Result :{a+b}")
def subtract(a,b):
    print(f"Result :{a-b}")
def multiply(a,b):
    print(f"Result :{a*b}")
def divide(a,b):
    print(f"Result :{a/b}")

a = int(input("Enter the number 1: "))
b = int(input("Enter the number 2: "))
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
choice = int(input("Enter the choice :"))
if choice == 1:
        add(a,b)
elif choice == 2:
        subtract(a,b)
elif choice == 3:
        multiply(a,b)
elif choice == 4:
        divide(a,b)
else:
        print("invalid choice!")




