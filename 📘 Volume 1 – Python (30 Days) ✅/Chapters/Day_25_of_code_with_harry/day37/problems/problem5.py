# Write a function that returns inside except and still executes finally.\\
def return_fuction():
    try:
        value = int(input("enter :"))
    except:
        return 90
    finally:
        print("Still executed")

print(return_fuction())