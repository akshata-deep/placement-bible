# Shopping Bill

# Take input for:

# Item 1 price
# Item 2 price
# Item 3 price

# Calculate:

# Total
# GST = 18%
# Final Bill

# Print a proper bill.

iteam1 = int(input("Enter the prize of first item : "))
iteam2 = int(input("Enter the prize of second item : "))
iteam3 = int(input("Enter the prize of third item : "))


total = iteam1 + iteam2 +iteam3
gst = (total * 18) / 100
final_bill = total + gst

print(f"=========== Shopping Bill ==========\n"
      f"FISRT ITEM : {iteam1}\n"
      f"SECOND ITEM : {iteam2}\n"
      f"THIRD ITEM : {iteam3}\n"
      f"TOTAL : {total}\n"
      f"FINAL BILL : {final_bill}\n\n"
      f"Note : the final bill includes 18% GST \n"
      f"=====================================")
