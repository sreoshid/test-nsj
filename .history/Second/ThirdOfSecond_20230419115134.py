x = int(input("Enter an integer that is the dividend: "))
y = int(input("Enter an integer that is the divisor: "))

class ZeroDivisionError(Exception):
    pass

def division(x,y):

    try:
        Quotient = x // y
        Remainder = x % y
        
    except ZeroDivisionError:
        print("Cannot divide by 0!")

    else:
        return Quotient, Remainder
    
    Quotient = division(x,y)[]
    
    print("Quotient is: ", division(x,y).Quotient)
    print("Remainder is: ",division(x,y).Remainder)


