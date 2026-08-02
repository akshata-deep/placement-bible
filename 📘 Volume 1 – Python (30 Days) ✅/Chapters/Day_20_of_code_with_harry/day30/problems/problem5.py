def printing_numbers(num):
    if num == 1:
        print(num)
    else:
        print(num)
        printing_numbers(num - 1)

num = 6
printing_numbers(num)