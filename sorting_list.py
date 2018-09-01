element_count = int(input("Enter no of elements : "))
input_list1 = []
for number in range(element_count):
    input_list1.append(int(input("Enter any element : ")))
for element in range(0, len(input_list1)):
    for element1 in range(element+1, len(input_list1)):
        if input_list1[element] > input_list1[element1]:
            temp_var = input_list1[element]
            input_list1[element] = input_list1[element1]
            input_list1[element1] = temp_var
print("List after sorting in ascending order = ", input_list1)
input_list1.reverse()
print("List after sorting in descending order = ", input_list1)
    
