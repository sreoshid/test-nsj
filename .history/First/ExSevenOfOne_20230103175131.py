input_string = input("Enter a string: ")
listForinput_string = input_string.split(" ")
listForDuplicates = []
print(listForinput_string)
for i in listForinput_string:
    if listForinput_string.count(i) > 1:
        list = listForDuplicates.append(i)
        print(list)
        unique_duplicates = set(list)
        stringOfduplicateValues = str(unique_duplicates)
        print ("The duplicate values are: ",stringOfduplicateValues)

