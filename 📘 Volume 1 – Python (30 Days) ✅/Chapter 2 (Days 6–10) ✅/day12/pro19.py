# Create a simple login system:

# Correct username and password → "Login Successful"
# Otherwise → "Invalid Credentials"

username_given = "Akshata"
password_give = "hello_akshata"



username = input("Enter the username :")
password = input("Enter the password :")

if username == username_given and password == password_give:
    print("LOGIN SYCCESSFUL")
else:
    print("INVALID CREDENTIALS")