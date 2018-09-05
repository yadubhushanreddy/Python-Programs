user_input = input("Enter any String : ")   #yadu    bhushan        hello
space_count = 0
string_without_spaces = ''
for char in user_input:
    if char == ' ' and space_count < 1:
        string_without_spaces += char
        space_count += 1
    elif char != ' ':
        string_without_spaces += char
        space_count = 0

print("String with out duplicate spaces = ", string_without_spaces)
#print("String without duplicate spaces = ", " ".join(user_input.split()))

