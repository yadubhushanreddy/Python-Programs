input_str = "this is sample 192.12.132.12 string"
ip_addr = ''
str_string = ''
for char in range(0, len(input_str)):
    if input_str[char].isdigit() or input_str[char] == '.':
        ip_addr = ip_addr + input_str[char]
    elif input_str[char].isalpha():
        str_string = str_string + input_str[char]
print("Ip address found in the given string = ", ip_addr)
print("String found = ", str_string)
