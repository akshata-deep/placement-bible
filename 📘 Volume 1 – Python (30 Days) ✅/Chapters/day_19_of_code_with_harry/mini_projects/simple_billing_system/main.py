customer_name = input("Enter the name : ")
product_name = input("Enter the  product name : ")
quantity = int(input("Enter the quantity : "))
price = int(input("Enter the price : "))

total_bill = price*quantity
print(f"================ Simple Billing System ================\n"
      f"Hello {customer_name} !\n\n"
      f"Product name : {product_name}\n"
      f"Quantity : {quantity}\n"
      f"Price : {price}\n\n"
      "-------------------------------------------\n"
      f"Total Bill : {total_bill:.2f}")