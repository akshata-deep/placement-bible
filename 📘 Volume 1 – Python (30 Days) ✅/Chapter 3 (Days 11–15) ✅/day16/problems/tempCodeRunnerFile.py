words = "a","e","i","o","u"
tell_me = input("Enter the word :")
for char in tell_me:
    for l in words:
        if char == l:
            print(char)
