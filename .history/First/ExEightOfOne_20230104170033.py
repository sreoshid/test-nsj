input_number = list(input("Enter five numbers from 1 to 10: "))
input_number = list(map(int, input_number))
print(input_number)
for num in input_number:
    for i in num:
        print(num, end=" ")
        print("\n")
    # if (i != 0):
        
    #     # i = [i]*i
        
    #     # listtostr = ' '.join(map(str,i))
    #     print ([i]*i)

