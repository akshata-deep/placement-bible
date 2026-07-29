# 3. Shopping Cart Function
# Use *args.
# Input multiple product prices:
# Example:
# 100, 200, 300, 500
# Return total amount.

def shopping_card(*amounts):
    total = sum(amounts)
    return total

print("WELLCOME TO SHOPPING CARD CALCULATER!..\n" 
      "----------------------------------------------------------")

amount_1 = int(input("Enter the first amount :"))
amount_2 = int(input("Enter the second amount :"))
amount_3 = int(input("Enter the third amount :"))
amount_4 = int(input("Enter the fouth amount :"))
amount_5 = int(input("Enter the first amount :"))
amount_6 = int(input("Enter the first amount :"))
total_amount = shopping_card(amount_1,amount_2,amount_3,amount_4,amount_5,amount_6)
print(f"Total amount of the shoppin card is :{total_amount}\n"
      f"----------------------------------------------------------")


