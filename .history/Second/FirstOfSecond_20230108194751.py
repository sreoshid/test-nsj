UserString = input("Enter three words in a sentence separated by comma: ").split(",")
print(UserString)
# list = UserString.repl_delim='**'
string = *UserString, sep=','
print(string)
UserOutput = string.replace(' ','**')


print("Output for each word separated by **: ",UserOutput)