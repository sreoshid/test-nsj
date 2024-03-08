Rows = int(input("Enter the number of rows to print the pattern: "))
for i in range(1, Rows+1):
    print ("*"*i)
    print(" "*(Rows-i), end="")