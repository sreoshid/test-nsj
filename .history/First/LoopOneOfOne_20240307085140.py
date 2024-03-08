#Exercise 1: Print First 10 natural numbers using while loop
# numbers = 1
# while(numbers<=10):
#     print(numbers)
#     numbers = numbers + 1

# n = 1
# while(n <=10):
#     print(n)
#     n=n+1

# Print the following pattern
# 1  2  
# 1  2  3  
# 1  2  3  4  
# 1  2  3  4  5  
# i=5

# for i in range(1,i+1,1):
#     for j in range(1,i+1,1):
#         print(j, end=" ")
#         j = j+1
#     print("")

#Answer: 
# i=5
# for i in range(1,i+1,1):
#     for j in range(1,i+1):
#         print(j,' ',end ='')
#     print()

# Calculate the sum of all numbers from 1 to a given number
    

num = 10

while(num<=10):
    total = num+1

print(total)











# num = int(input('Enter a number: '))
# sum = 0
# for i in range(1,num+1,1):
#     sum = sum + i

# print("Sum is: ",sum)

#OR..Another solution

# num = int(input('Enter a number: '))
# s = sum(range(1,num+1))
# print("Sum is: ",s)

#Write a program to print multiplication table of a given number

# num = int(input("Enter a number: "))
# for i in range(1,11):
#     m = num*i
#     print(num,"*",i,"=",m)

# Exercise 5: Display numbers from a list using loop
    # The number must be divisible by five
    # If the number is greater than 150, then skip it and move to the next number
    # If the number is greater than 500, then stop the loop

# list = []
# for i in range(11):
#     input_number = int(input("Enter number: "))
#     list.append(input_number)
# for i in list:
#     if(i<150 | i>150):
#         if (i<500):
#             if (i%5 == 0):
#                 print(i,end = '')
        

# Exercise 6: Count the total number of digits in a number

# number =  int(input("Enter a big number: "))
# count_num = 0
# while(number != 0):
#     number = number // 10
#     count_num = count_num +1
# print(count_num)

#Write a program to use for loop to print the following reverse number pattern
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

# num = 5
# for i in range(num,0,-1):
#     for j in range(i,0,-1):
#         print(j,' ',end='')
#     print()


#Print list in reverse order using a loop
# new_list1 = reversed(list1)
# for i in new_list1:
#     print(i)

# list1 = [10, 20, 30, 40, 50]

# size = len(list1)
# for i in range(size-1,-1,-1):
#     output_list1 = list1[i]
#     print(output_list1)

# Display numbers from -10 to -1 using for loop

# num = -10
# for i in range(-10,0,1):
#     print(i)

#Display Fibonacci series up to 10 terms
# num1,num2 = 0,1
# for i in range(10):
#     print(num1, " ",end = "")
#     num1, num2 = num2, num1 + num2

#Calculate the factorial of 5

# num = 5
# factorial = 1
# for i in range(1,num+1,1):
#     factorial = factorial * i
# print(factorial)
    
#Write a program to calculate the sum of series up to n term. 
#For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

# n = 5
# x = 2
# sum_sequence = 0
# for i in range(0,5):
#     sum_sequence = x + sum_sequence
#     x = x*10 + 2
# print(sum_sequence)

#Write a program to print the following start pattern using the for loop
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

# start = 1
# end = 6

# for i in range(1,6,1):
#     print ('*'*i)

# for i in range(4,0,-1):
#     print('*'*i)
# for i in (end-1,start+1,-1):
#     print('*'*i)



# Take the end number like 5 and result = num
# find out the number prev to 5 ===(num -1) here num = 4 and prev = 3
# set result = result * prev= 20
# set num = prev
# go to step 2 until num > 0
# num = 5
# factorial = num
# while(num>1):
#     prev = num -1
#     factorial = factorial * prev
#     num = prev
# print(factorial)
#################################################################################################
# FUNTIONS

#Write a program to create a function that takes two arguments, name and age, and print their value.

# def nameAge(name,age):
#     return print("Name is: ",name), print("Age is: ",age)

# name = input("Enter the name: ")
# age = input("Enter the age: ")

# nameAge(name,age)



    
    

