num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))
num5 = int(input("Enter the fifth number: "))

listOfNums = [num1,num2, num3, num4, num5]
for i in listOfNums:
    if i%5 == 0:
        output_list = [i].append()
    else:
        continue
print("List of input numbers divisible by 5: ",output_list)
