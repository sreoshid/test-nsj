input = [int(x) for x in input("Enter three numbers separated by comma for which you would like to see the multiplication table from 1-10: ").split(',')]
# print(input)
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in input:
    # for num in range(1,10):
        list_result = [num*i for num in list]
        # print(list_result)
        result = print(*list_result, sep=" ")


