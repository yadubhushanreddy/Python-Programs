def find_numerics():
    user_input = input("Enter any string : ")
    numerics, numerics_no= '', 0
    for char in user_input:
        if char.isnumeric():
            numerics_no += 1
            numerics += char
    print("No of numerics = ", numerics_no)
    print("Numerics found = ", numerics)

find_numerics()
            
