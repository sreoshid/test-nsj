UserString1,UserString2,UserString3 = input("Enter three words in a sentence separated by comma: ")
list = [UserString1,UserString2,UserString3].repl_delim='**'


print("Output for each word separated by **",list)