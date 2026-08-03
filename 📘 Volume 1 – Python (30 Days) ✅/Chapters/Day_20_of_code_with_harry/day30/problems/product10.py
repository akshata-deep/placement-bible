def sum_numbers(n,product):
    if n == 1:
        return product
    else:
        product = product + n
        result = sum_numbers(n-1,product)
        return result

product = 1
n = 5
product = sum_numbers(n,product)
print(product)






def sum_numbers(n):
    if n == 1:
        return 1
    total = sum_numbers(n-1)
    return total +n


print(sum_numbers(6))
    