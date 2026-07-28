original_user = "Akshata"
original_password = "python i am in"

for i in range(0,4):
    if i == 3:
        print("Account Locked")
        break
    user = input("Enter the user name:")
    password = input("Enter the password:")


    if user == original_user and password == original_password:
        print("Login Successfull")
        break