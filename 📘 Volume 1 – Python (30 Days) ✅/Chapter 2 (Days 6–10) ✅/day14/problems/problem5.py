
import time 
timeing = int(time.strftime("%H"))
name = input("Enter the name :")
if timeing <= 12 :
    print(f"good morning {name}!")
elif timeing <= 5:
    print(f"good afternoon {name}!")
else:
    print(f"good evening {name}!")