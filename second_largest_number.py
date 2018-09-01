no_of_elements = int(input("Enter no of elements : "))
input_list = []
max_number, second_max_number = 0, 0
for number in range(no_of_elements):
    input_list.append(int(input("Enter any number : ")))
for element in range(0, len(input_list)):   #12 3 24 32 25
    if max_number < input_list[element]:
        second_max_number = max_number
        max_number = input_list[element]
    elif second_max_number < input_list[element]:
        second_max_number = input_list[element]
print("Maximum number = ", max_number)
print("Second maximum number = ", second_max_number)
