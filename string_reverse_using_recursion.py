def reverse_string(length):
    print(name[length - 1], end = "")
    if length > 1:
        reverse_string(length - 1)
    print(name[length - 1], end = "")


name = 'bhushan'
reverse_string(len(name))
