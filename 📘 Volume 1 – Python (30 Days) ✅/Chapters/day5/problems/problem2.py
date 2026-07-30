# write a program to greet all the person names stored in a lst "l" and which start with S
# l = ["Harry","Soham","Sachin","Rahul"]

l = ["Harry","Soham","Sachin","Rahul"]
for name in l:
    if name.startswith("S"):
        print("hello",name)

