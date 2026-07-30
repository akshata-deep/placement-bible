


def view_product(products):
    serial_number = 0
    for i in products:
        serial_number += 1
        print(f"{serial_number}.{i}")

def search_product(products):
    name = input("Enter the product : ")
    if name in products:
        print("Product Available")
    else:
        print("Product Not Available")

def add_product(products):
    name = input("Enter the product : ")
    if name in products:
        print("This product is already in list")
    else:
        products.append(name)
        print("Product is added !")

def remove_procuct(products):
    name = input("Enter the  product : ")
    if name in products:
        products.remove(name)
        print("product is removed !")
    else:
        print("This product is not there in list")

products = ["Laptop","Mouse","Keyboard","Monitor","Headphones","Printer"]

print("========== SHOPPING CART ==========\n"
      "1. View Products\n"
      "2. Search Product\n"
      "3. Add Product\n"
      "4. Remove Product\n"
      "5. Exit\n")


while True:
    option = int(input("\nEnter the option : "))
    if option == 1:
        view_product(products)

    elif option == 2:
        search_product(products)

    elif option == 3:
        add_product(products)

    elif option == 4:
        remove_procuct(products)
    elif option == 5:
        break
    else:
        print("invalid option !")
