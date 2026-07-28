original_password = "python123"


for i in range(4):
    user_password = input("Enter the password : ")
    if user_password == original_password:
        print("Access Granted")
        break
    if i == 3:
        print("Access Denied")
    