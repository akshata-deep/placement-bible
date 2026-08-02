def printing_number(num):
    if num == 1:
        print(num)
    else:
        printing_number(num - 1)
        print(num)



num = 9
printing_number(num)