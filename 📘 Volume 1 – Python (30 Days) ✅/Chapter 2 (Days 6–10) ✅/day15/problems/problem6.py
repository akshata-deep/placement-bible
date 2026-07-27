# Write a Menu Selection Program.

# Menu:

# 1. Start Game
# 2. Load Game
# 3. Settings
# 4. Exit

# Requirements:

# Ask the user for a choice.
# Use match-case.
# Print the correct option.
# Print "Invalid Choice" for anything else.

# print("Menu:\n"
#       "1. Start Game\n"
#       "2. Load Game\n"
#       "3. Settings\n"
#       "4. Exit")
menu_options = int(input("Enter the option: "))

match menu_options :
    case 1:
        print("1. Start Game")
    case 2:
        print("2. Load Game")
    case 3:
        print("3. Settings")
    case 4:
        print("4. Exit")
    case _:
        print("Invalid option")