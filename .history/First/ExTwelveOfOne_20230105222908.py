Salary = float(input("Enter the Salary: "))
tax1=0
tax2=0
if Salary<=10000:
    print("No income tax")
else:
    if Salary%10000 != 0.00:
        tax1 = 1000
        Salary = Salary-10000
        if Salary > 0.00:
            tax2 = Salary*0.2
Income_tax = tax1+tax2
print("Total Income tax to be deposited: ",Income_tax)