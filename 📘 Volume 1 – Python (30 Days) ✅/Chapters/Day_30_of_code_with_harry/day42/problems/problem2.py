# Print student names with numbering starting from 1.

names = ["Alex", "Ben", "Charlie", "Daisy", "Ethan"]
for index, name in enumerate(names, start=1):
    print(f"{index} : {name}")