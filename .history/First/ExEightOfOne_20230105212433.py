input_number = input("Enter five numbers from 1 to 10: ")
input_number = list(map(int, input_number))
# numbers = []
print(input_number)
for num in input_number:
        print ([num]*num)

