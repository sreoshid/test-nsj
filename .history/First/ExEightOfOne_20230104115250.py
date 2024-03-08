input_number = list(input("Enter five numbers from 1 to 10: "))
input_number = list(map(int, input_number))
print(input_number)
for i in input_number:
    if (i != 0):
        listtostr = ' '.join(map(str,i))
        print (i*i)

