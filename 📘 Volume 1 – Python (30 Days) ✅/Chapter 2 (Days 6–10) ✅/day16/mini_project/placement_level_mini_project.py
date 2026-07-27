count = int(input("Enter number of students :"))
names = []
for i in range (1,count+1):
    name = input(f"Student {i}:")
    names.append(name)
indexing = 0
print(f"========== ATTENDANCE REPORT =========\n\n"
      f"Roll No   Name\n"
      f"--------------------")
for i in range(1,count+1):
        print(f"{i}         {names[indexing]}")
        indexing += 1
print(f"\nTotal Students : {count}")