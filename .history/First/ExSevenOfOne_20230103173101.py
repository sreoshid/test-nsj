input_string = input("Enter a string: ")
listForinput_string = input_string.split(",")
for i in listForinput_string:
    if listForinput_string.count(i) > 1:
        print(i)
