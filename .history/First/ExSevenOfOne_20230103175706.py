input_string = input("Enter a string: ")
listForinput_string = input_string.split(" ")
listForDuplicates = []
for i in listForinput_string:
    if listForinput_string.count(i) > 1:
        listForDuplicates.append(i)
unique_duplicates = set(list)
stringOfduplicateValues = str(unique_duplicates)
print ("The duplicate values are: ",stringOfduplicateValues)       

