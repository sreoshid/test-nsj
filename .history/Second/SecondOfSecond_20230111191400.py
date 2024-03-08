number = int(input("Enter a decimal number to be converted to octal: "))
octal_number = number%8
octal = octal_number.reversed()
print("The number converted from decimal to octal is: ",octal)