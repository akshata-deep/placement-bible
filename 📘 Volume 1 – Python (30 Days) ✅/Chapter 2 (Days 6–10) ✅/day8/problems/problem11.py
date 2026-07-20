# Without using count(), write a program to find how many times 35 appears in the list.

marks = [35, 40, 35, 90, 60, 35, 80]
counting_35 = 0
for i in range (0,7):
    if marks[i] == 35:
        counting_35 += 1
    else:
        continue

print(counting_35)