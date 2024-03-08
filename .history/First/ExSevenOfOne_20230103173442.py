input_string = input("Enter a string: ")
listForinput_string = input_string.split(",")
print(listForinput_string)
for i in listForinput_string:
    if listForinput_string.count(i) > 1:
        print(i)
