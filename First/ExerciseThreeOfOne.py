User_Input = str(input("Enter a string: "))
str_length = len(User_Input)
for i in range(0,str_length-1):
    if i%2 == 0:
        print("Printing only the letters at even indices: ",User_Input[i])
        continue