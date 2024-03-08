User_Input = str(input("Enter a string: "))
str_length = len(User_Input)
for i in range(User_Input.rindex(0),User_Input.rindex(str_length-1)):
    if i%2 == 0:
        print("Printing only the letters at even indices: ",User_Input.rindex(i))
        
    continue