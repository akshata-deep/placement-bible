def sum_numbers(n,sum):
    if n == 1:
        sum *= n
        return sum
    else:
        sum *= n
        result = sum_numbers(n-1,sum)
        return result


    

sum = 0
result = sum_numbers(3,sum)
print(result)