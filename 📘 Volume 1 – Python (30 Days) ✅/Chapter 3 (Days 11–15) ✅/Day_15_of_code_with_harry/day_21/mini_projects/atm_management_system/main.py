# ========== ATM ==========
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Mini Statement
# 5. Exit


def check_balance(amount_in_bank):
    print(f"current_balance : {amount_in_bank}")
    return amount_in_bank

def deposit(amount_in_bank,last_deposite):
    add_amount = int(input("Enter the amount : "))
    if add_amount <= 0:
        print("0 or \'-\' values are not allowed")
        return amount_in_bank,last_deposite
    else:
        amount_in_bank += add_amount
        print("DONE!")
        return amount_in_bank,add_amount

def withdraw(amount_in_bank,last_withdraw):
    remove_amount = int(input("Enter the amount:"))
    if remove_amount > amount_in_bank:
        print(f"your bank balance is {amount_in_bank}")
        return amount_in_bank,last_withdraw
    elif amount_in_bank <= 0 :
        print("your bank balance is 0")
        return amount_in_bank,last_withdraw
    elif remove_amount <= 0:
        print("0 or \'-\' values are not allowed")
        return amount_in_bank,last_withdraw
    else:
        amount_in_bank -= remove_amount
        print("DONE !")
        return amount_in_bank,remove_amount

def mini_statement(amount_in_bank,add_amount,remove_amount):
    print(f"========== MINI SATEMENT ==========\n"
          f"CURRENT BALANCE : {amount_in_bank}\n"
          f"LAST DEPOSIT    : {add_amount}\n"
          f"LAST WITHDRAWAL : {remove_amount}")


amount_in_bank = 50000
add_amount = 0
remove_amount = 0
while True:
    option = int(input("Enter the option : "))
    if option == 1:
        amount_in_bank = check_balance(amount_in_bank)
    elif option == 2:
        amount_in_bank,add_amount = deposit(amount_in_bank,add_amount)
    elif option == 3:
        amount_in_bank,remove_amount = withdraw(amount_in_bank,remove_amount)
    elif option == 4:
        mini_statement(amount_in_bank,add_amount,remove_amount)
    elif option == 5:
        break
    else:
        print("invalid option !")






