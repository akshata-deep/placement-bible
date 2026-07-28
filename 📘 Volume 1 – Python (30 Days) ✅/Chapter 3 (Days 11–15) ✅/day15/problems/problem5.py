# 1 → Withdraw
# 2 → Deposit
# 3 → Balance Check
# 4 → Exit

# Use match-case.




atm_option = int(input("Enter the options :"))



match atm_option:

    case 1:

        print("1 → Withdraw")

    case 2:

        print("2 → Deposit")

    case 3:

        print("3 → Balance Check")
    case 4:

        print("4 → Exit")

    case _:

        print("invalid option!")