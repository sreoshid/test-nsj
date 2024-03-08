number = int(input("Enter a decimal number to be converted to octal: "))
octal_number = number%8
octal = reversed(octal_number)
print("The number converted from decimal to octal is: ",octal)