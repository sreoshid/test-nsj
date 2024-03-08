num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num3 = input("Enter the third number: ")
num4 = input("Enter the fourth number: ")
num5 = input("Enter the fifth number: ")

listOfNums = [num1, num2, num3, num4, num5]
for i in listOfNums:
    if i%5 == 0:
        output_list = list().append(i)
    else:
        continue
print("List of inout numbers divisible by 5: ",output_list)
