def product_numbers(n,product):
    if n == 1:
        return product
    else:
        product = product * n
        result = product_numbers(n-1,product)
        return result

product = 1
n = 5
product = product_numbers(n,product)
print(product)
