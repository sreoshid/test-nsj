x = int(input("Enter an integer that is the dividend: "))
y = int(input("Enter an integer that is the divisor: "))

class ZeroDivisionError(Exception):
    pass

def division(x,y):

    try:
        Quotient = x / y
        Remainder = x % y
        
    except ZeroDivisionError:
        print("Cannot divide by 0!")
        return None, None

    else:
        return Quotient, Remainder
    
Quotient = division(x,y)[0]
Remainder = division(x,y)[1]
    
print("Quotient is: ", Quotient)
print("Remainder is: ",Remainder)


