x = int(input("Enter an integer that is the dividend: "))
y = int(input("Enter an integer that is the divisor: "))

class ZeroDivisionError(Exception):
    def __init__(self, message):
        self.message = message

def division(x,y):
    try:
        # Quotient = x // y
        # Remainder = x % y
    except ZeroDivisionError as e:
        print("Cannot divide by 0! "+e)
        return None, None

    return Quotient, Remainder

    
print("Quotient is: ", division(x,y)[0])
print("Remainder is: ",division(x,y)[1])


