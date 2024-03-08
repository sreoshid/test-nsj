#Create a list of the cubes of numbers from 1 to 10.

numbers = range(1,10+1)

cubes = [num**3 for num in numbers]

print(cubes)

#Generate a list of odd numbers between 1 and 30.

numbers = range(1, 30+1)

odd_numbers = [num for num in numbers if(num%2!=0)]

print(odd_numbers)

#Convert a string to a list containing lowercase versions of its characters.

string = "Sreoshi DasGupta"

