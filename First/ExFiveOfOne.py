user_input = str(input("Enter the first string: "))
user_input1 = str(input("Enter the second string: "))
if user_input == user_input1:
    user_input1 = str(input("Enter a different string from the first one: "))
new_string1=user_input[4:]
new_string2=user_input[2:]
print("Replaced string for first input string  is: ",new_string1)
print("Replaced string for second input string  is: ",new_string2)