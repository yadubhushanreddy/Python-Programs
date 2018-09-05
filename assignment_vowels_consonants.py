def separate_vowels_consonants():
    first_input = input("Enter first input : ")    #yadu
    first_input_consonants = ''
    second_input = input("Enter second input : ")
    second_input_vowels = ''
    
    #second_input = input("Enter second input : ") 
    if len(first_input) > 0:
        list1 = list(first_input)
        #print("List1 = ", list1)
        for element in range(0, len(list1)):
            if list1[element] == 'a' or list1[element] == 'e' or list1[element] == 'i' or list1[element] == 'o' or list1[element] == 'u':
                list1[element] = '$'
            else:
                first_input_consonants = first_input_consonants + list1[element]
    print("First input after replacing vowels = ", "".join(list1))
    print("Consonants from first input = ", first_input_consonants)

    if len(second_input) > 0:
        list2 = list(second_input)

        for element in range(0, len(list2)):
            if list2[element] != 'a' and list2[element] != 'e' and list2[element] != 'i' and list2[element] != 'o' and list2[element] != 'u':
                list2[element] = '#'
            else:
                second_input_vowels = second_input_vowels + list2[element]
    print("Second input after replacing consonants = ", "".join(list2))
    print("Vowels from second input = ", second_input_vowels)
    print("Third string (Consonants from first input + Vowels from second input) = ", (first_input_consonants + second_input_vowels).upper())

separate_vowels_consonants()
