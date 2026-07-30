# Count how many vowels are present in a string using only a while loop.



word = input("Enter the word:")
vowels = ['a','e','i','o','u']
i =0
count = 0
while i<len(word):
    if word[i] in vowels:
        count +=1
    i += 1
print(f"the count of the vowels in the word ({word}):{count}")
