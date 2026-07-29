# Question 8 — Deadly High 🏢 (Placement Level)
# 📌 Problem: Bank Account System

# Create a menu-driven program using functions:

# Deposit
# Withdraw
# Check Balance
# Exit

# Requirements:

# Use separate functions.
# Use return wherever appropriate.
# Prevent withdrawing more than the available balance.
# Continue until the user chooses Exit.


def deposit(amount_in_bank):
        add = int(input("Enter the amount : "))
        if add < 0:
            print("you can\'t deposite a \"-\" amounts")
            return amount_in_bank
        else:
            amount_in_bank += add 
            print("Done!")
            return amount_in_bank

def withdraw(amount_in_bank):
        take = int(input("Enter the amount : "))
        if take > amount_in_bank :
              print("insaficiant balance")
              return amount_in_bank
        elif take < 0:
              print("invalid!")
              return amount_in_bank
        else:
            amount_in_bank -= take
            print("Done!")
            return amount_in_bank

def check_balance(amount_in_bank):
        return amount_in_bank





print("1.Deposit\n2.Withdraw\n3.Check Balance\n4.Exit")
# option = int(input("Enter the option : "))
amount_in_bank = 50000
while True:
    option = int(input("Enter the option : "))
    if option == 1:
            amount_in_bank = deposit(amount_in_bank)
            
    elif option == 2:
        if amount_in_bank <= 0:
            print("your balances is 0")
        else:
            amount_in_bank = withdraw(amount_in_bank)
           
    elif option == 3:
            amount_in_bank = check_balance(amount_in_bank)
            print(f"Your balances : {amount_in_bank}")
    elif option == 4:
        break
    else:
        print("Invalid Option!")