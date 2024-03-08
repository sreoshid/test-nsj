UserString = input("Enter three words in a sentence separated by comma: ").split(",")
print(UserString)
# list = UserString.repl_delim='**'
string = ' '
for i in UserString:
    string += '**'+i

print(string)
# UserOutput = string.replace(' ','**')


print("Output for each word separated by **: ",string)