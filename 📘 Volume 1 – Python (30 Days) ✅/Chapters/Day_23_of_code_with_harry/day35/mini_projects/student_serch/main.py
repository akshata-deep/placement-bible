students = ["Akshata", "Anu", "Rahul", "Amruta", "Kiran"]
name = input("Enter the name : ")

for i in range(5):
    if name == students[i]:
        print("found")
        break
else:
    print("not")
