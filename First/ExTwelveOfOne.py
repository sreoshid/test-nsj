Salary = float(input("Enter the Salary: "))
tax1=0
tax2=0
tax3=0
if Salary<=10000:
    print("No income tax")
elif Salary > 20000:
    tax1 = 0
    Salary = Salary -10000
    if Salary > 10000:
        tax2 = 10000*0.1
        Salary = Salary -10000
        if Salary>0:
            tax3 = Salary*0.2
    
Income_tax = tax1+tax2+tax3
print("Total Income tax to be deposited: ",Income_tax)