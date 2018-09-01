string = 'bhushan'
list1 = [char for char in string]
print(list1)
print(id(list1))

list2 = list(string)
print(list2)
print(id(list2))

list3 = [number for number in range(1, 100, 2)]
print(list3)

list4 = [number for number in range(1, 100) if number % 3 == 0 if number % 5 == 0]
print("Divisibles of 3 are ", list4)
