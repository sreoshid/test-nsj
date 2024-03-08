# sum=0
# num=10

# for i in range(1,num+1,1):
#     sum = sum + i

# print(sum)

#Write a program to print multiplication table of a given number

# num=9
# prod=0
# for i in range(1,num+1,1):
#     prod = i*num
#     print(prod)

# Exercise 5: Display numbers from a list using loop
    # The number must be divisible by five
    # If the number is greater than 150, then skip it and move to the next number
    # If the number is greater than 500, then stop the loop

list = [1, 10, 14, 30, 38, 55, 120, 25, 150, 455, 290, 500]
list2 =[]

for i in list:
    if i>500:
            break
    if i%5 == 0:
            if i>150:
                
                i = list[j+1]
            else:
                list2.append(i)
    
    for j in range(len(list)):
        

print(list2)
        
        