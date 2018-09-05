user_input = input("Enter any string : ")
list1 = [char for char in user_input]
list1.reverse()
reverse_string = "".join(list1)
print("Reverse of given string = ", reverse_string)
