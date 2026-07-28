# Ask the user to enter a word.

# Print every character.
# If the character is 'a', stop immediately using break.


word = input("Enter the word:")
for char in word:
    if char == 'a':
        break
    print(char)