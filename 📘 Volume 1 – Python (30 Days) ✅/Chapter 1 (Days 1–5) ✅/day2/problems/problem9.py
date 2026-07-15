#  Largest of 3


# method 1
a = int(input("enter the number 1:"))
b = int(input("enter the number 1:"))
c = int(input("enter the number 1:"))
largest = max(a,b,c)
print(f"the large number is : {largest}")

# method 2
a = int(input("enter the number 1:"))
b = int(input("enter the number 1:"))
c = int(input("enter the number 1:"))

if a>=b and a>=c :
    print("a is larger")
elif b>=a and b>=c :
    print("b is larger")
else :
    print("c is larger")
   