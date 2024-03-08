Number = str(input("Enter a three digit number: "))
Reversed_number = "".join(reversed(Number))
if Number == Reversed_number:
    print("The entered number is a Pallindrome")
else:
    print("Entered number is not a pallindrome")