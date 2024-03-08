input_number = int(input("Enter five numbers from 1 to 10: "))
input_number = list(input_number)
print(input_number)
for i in input_number:
    if (i != 0):
        print ([i]*i,"\n")

