def coding(coding_characters):
    try:
        if len(coding_characters) <= 0:
            raise IndexError("You can\'t use empty string")
        elif coding_characters == "abc" or coding_characters == "san":
            raise ValueError("\"abc\" or \"san\" is not allowed ")

        elif len(coding_characters) >=3:
            first_char = coding_characters[0]
            removed_word = coding_characters.replace(f"{first_char}","",1)
            final_word = removed_word + first_char
            final_word = "aks" + final_word + "san"
            print(final_word)
        else:
            first_char = coding_characters[0]
            removed_word = coding_characters.replace(f"{first_char}","",1)
            final_word = removed_word + first_char
            print(final_word)
    except Exception as e:
        print(e)

def decoding(decoding_characters):
    try:
        if len(decoding_characters) <= 0:
            raise IndexError("You can\'t use empty string")
        elif coding_characters == "abc" or coding_characters == "san":
            raise ValueError("\"abc\" or \"san\" is not allowed ")
        
        elif len(decoding_characters) >=3:
            f_removed = decoding_characters[3:]
            l_removed = f_removed[:-3]
            last_char = l_removed[-1]
            last_removed = l_removed[:-1]
            final_word = last_char +last_removed
            print(final_word)
        else:
            last_char = decoding_characters[-1]
            removed_word = decoding_characters.replace(f"{last_char}","",1)
            final_word = last_char + removed_word
            print(final_word)
    except Exception as e:
            print(e)
    

    




print("========== WELCOME TO CODING WORLD ==========\n"
      "1.CODING  \n"
      "2.DECODING \n"
      "3.EXIT")
while True:
    try:
        options = int(input("Enter the option :"))
        if options == 1:
            coding_characters = input("Enter the words : ")
            coding(coding_characters)
        elif options == 2:
            decoding_characters = input("Enter the words : ")
            decoding(decoding_characters)
        elif options == 3:
            break
        else:
            print("invalid option")
    except ValueError:
        print("ValueError ! please enter a number.")