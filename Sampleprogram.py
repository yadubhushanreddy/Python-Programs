list1 = [(1,"yadu"), [2,3.5], 3, 'bhushan']
list2 = []
for element in list1:
    if (type(element) is tuple) or (type(element) is list):
        for element1 in element:
            list2.append(element1)
    else:
        list2.append(element)
print(list2)
        
