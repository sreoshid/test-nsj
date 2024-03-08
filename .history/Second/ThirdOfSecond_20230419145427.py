x = input("Enter an integer that is the dividend: "))
y = int(input("Enter an integer that is the divisor: "))

class ZeroDivisionError(Exception):
    pass

def division(x,y):

    try:
        Quotient = x // y
        Remainder = x % y
        
    except ZeroDivisionError:
        print("Cannot divide by 0!")
        return None, None

    else:
        return Quotient, Remainder

    
print("Quotient is: ", division(x,y)[0])
print("Remainder is: ",division(x,y)[1])


