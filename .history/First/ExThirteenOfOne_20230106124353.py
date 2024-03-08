input1, input2, input3 = list(int(input("Enter three numbers for which you would like to see the multiplication table from 1-10: ")))
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in input:
    for num in list:
        list_result = i*num
        result = print(*list_result, sep=" ")


