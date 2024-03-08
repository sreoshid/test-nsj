input1 = int(input("Enter first number for which you would like to see the multiplication table from 1-10: "))
input2 = int(input("Enter second number for which you would like to see the multiplication table from 1-10: "))
input3 = int(input("Enter third number for which you would like to see the multiplication table from 1-10: "))
input = list(input1,input2,input3)
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in input:
    for num in list:
        list_result = i*num
        result = print(*list_result, sep=" ")


