name = "Artificial Intelligence"
lower_name = name.lower()
vowels = ["a","e","i","o","u"]
for char in lower_name:
    for j in vowels:
        if char == j:
            print(char)