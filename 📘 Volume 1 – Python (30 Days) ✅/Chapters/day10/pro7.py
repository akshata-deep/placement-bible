# Requirements:

# Convert all prices.
# Calculate:
# Total
# GST Amount
# Final Bill
# Print all values with proper formatting.
# Print the data type of every calculated value.



item1 = "799"
item2 = "1299"
item3 = "499"
gst = 18


item1_int = int(item1)
item2_int = int(item2)
item3_int = int(item3)

total = item1_int + item2_int + item3_int
final_bill = item1_int + item2_int + item3_int +gst
print(f"Total : {total}\n"
      f"GST Amount : {gst}\n"
      f"Final Bill : {final_bill}\n\n"
      f"TYPES:\n"
      f"Type of total : {type(total)}\n"
      f"Type of final bill : {type(final_bill)}")