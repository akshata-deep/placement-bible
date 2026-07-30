original_name = "Akshata"
original_password = "python"

for i in range (3):
    user_name = input("Enter the name :")
    user_password = input("Enter the password :")
    if user_name == original_name and user_password == original_password:
        print("Login Successful\nWelcome Akshata")
        break
else:
    print("Account Locked")
    