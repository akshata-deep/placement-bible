# Find the index of a particular name using enumerate().

names = ["Alex", "Ben", "Charlie", "Daisy", "Ethan"]
for index,name in enumerate(names):
    if name == "Daisy":
        print(f"Found! \n{name} index is {index}")
