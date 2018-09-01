list1 = [23, 21, -34, 32, 12]
max_number = 0
for number in range(0, len(list1)):
    if max_number < list1[number]:
        max_number = list1[number]
print("Maximum number = ", max_number)
