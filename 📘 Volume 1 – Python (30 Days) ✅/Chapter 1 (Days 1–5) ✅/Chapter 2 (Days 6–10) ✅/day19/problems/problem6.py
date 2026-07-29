# Ask the user for a sentence.

# Skip all spaces using continue.


sentence = input("Enter the sentences :")
for char in sentence:
    if char == " ":
        continue
    print(char,end="")