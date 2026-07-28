# =========================
# WELCOME
# =========================

# Current Time : 18:20:55

# Good Evening Akshata

# Hope you are having a wonderful day.

# =========================




import time 
timeing = int(time.strftime("%H"))
current_time = time.strftime("%H:%S:%M")
name = input("Enter the name :")
print(f"=========================\n"
      f"WELCOME\n"
      f"=========================\n\n"
      f"Current Time : {current_time}\n")
if timeing <= 12:
    print(f"good morning {name}!\n")
elif timeing <= 5:
    print(f"good afternoon {name}!\n")
else:
    print(f"good evening {name}!\n")
greeting = "Hope you are having a wonderful day!"
print(f"{greeting}\n"
      f"=========================")