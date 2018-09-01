no_of_elements = int(input("Enter number of elements : "))
input_list = []
for number in range(0, no_of_elements):
    input_list.append(int(input("Enter any number : ")))
input_list.sort(reverse = True)
print("Second largest number is : ", input_list[1])
