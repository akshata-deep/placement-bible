correct_pin = "1234"
for i in range (3):
    entered_pin = input("Enter the pin : ")
    if entered_pin == correct_pin:
        print("Login Successful\nWelcome to ATM")
        break
    if i == 2:
        print("Card Blocked")
    else:
        print("Incorrect PIN")