User_Input = str(input("Enter a string: "))
for i in range(0,len(User_Input)):
    if i%2 == 0:
        print("Printing only the letters at even indices: ",User_Input.rindex(i))
        
    continue