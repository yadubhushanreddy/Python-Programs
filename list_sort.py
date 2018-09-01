no_of_elements = int(input("Enter number of elements : "))
input_list = []
for input_number in range(no_of_elements):
    input_list.append(int(input("Enter number : "))
for element in range(0, len(input_list)):
                      for element1 in range(1, len(input_list)):
        if(input_list[element] > input_list[element1]):
            temp = input_list[element]
            input_list[element] = input_list[element1]
            input_list[element1] = temp
print("Sorted list = ", input_list)
                      
    
