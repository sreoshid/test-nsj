var1 = "Sreoshi "
print(var1*2)


var2 = 10e3
print(var2)


print("##############2nd part##############")

name = "Sreoshi"
greetings = f"Hello, {name}"

print(greetings)


greetings_formatted = "{}'s sister is {}"
print(greetings_formatted.format("Nishant", "Shivangi"))


print("#####################3rd part############")

size_input = int(input("Enter the size of your house area in square feet: "))
square_metres = size_input/10.8

print(f"The size of your house which is {size_input} square feet, equals to {square_metres} square metres")

print("#####################4th part############")

size_input = int(input("Enter the size of your house area in square feet: "))
square_metres = size_input/10.8

print(f"The size of your house which is {size_input} square feet equates to {square_metres:.2f} square metres")

print("#####################5th part############")

user_age = int(input("Enter your age: "))
number_of_days = user