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

listOfString = [x for x in string if x.islower()]

print(listOfString)

#Create a list of consonants found in a given string.

string = "Sreoshi DasGupta"

listOfconsonants = [x for x in string if x not in ("a","e","i","o","u")]

print(listOfconsonants)

#Generate a list of lengths of words in a sentence.

sentence = "I am Sreoshi. I am a QA"
 
lengthOfWords = [len(word) for word in sentence.split()]

print(lengthOfWords)

#Create a list of Fibonacci numbers less than 100.

def fibonacci(range):
    series = [0,1]
    while series[-1] + series[-2] < range:
        series.append(series[-1]+series[-2])
    return series

fibonacci_number = [x for x in fibonacci(100)]

print(fibonacci_number)

#Generate a list of tuples containing all possible pairs of numbers from two lists [1, 2, 3] and [4, 5, 6].

list1 = []