user_input = input("Enter any name : ")
reverse_string = ''
for number in range(len(user_input)-1, -1, -1):
    reverse_string = reverse_string + user_input[number]
print("Reverse of a string = ", reverse_string)
