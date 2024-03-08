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

sentence = list("I am Sreoshi. I am a QA"
print(sentence)
 
# lengthOfWords = [len(word) for word in sentence.split()]

# print(lengthOfWords)