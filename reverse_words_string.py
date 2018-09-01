user_input = input("Enter any string : ")
words_reverse = ''
for string in user_input.split():
    for number in range(len(string)-1, -1, -1):
        words_reverse += string[number]
    words_reverse += " "
print("Reverse of given words = ", words_reverse)
