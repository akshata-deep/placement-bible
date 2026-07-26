# 🟠🔥 Deadly Moderate ×1

# Also display current time.

# Example

# Current Time : 18:42:31
# Good Evening Akshata




import time 
timeing = int(time.strftime("%H"))
current_time = time.strftime("%H:%S:%M")
name = input("Enter the name :")
print(f"Current Time : {timeing}")
if timeing <= 12:
    print(f"good morning {name}!")
elif timeing <= 5:
    print(f"good afternoon {name}!")
else:
    print(f"good evening {name}!")