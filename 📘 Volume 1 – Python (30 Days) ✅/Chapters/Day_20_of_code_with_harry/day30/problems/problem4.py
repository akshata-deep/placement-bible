def sum_of_numbers(num,storing):
    if num == 1:
        return storing
    else:
        sum_of_numbers(num-1,storing)
        storing += num
        return storing

num = 5
storing = 0
total = sum_of_numbers(num, storing)
print(total)