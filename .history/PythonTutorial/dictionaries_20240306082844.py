friends_ages = {"Rolf" : 30, "Adam" : 27, "Jene" : 24}

print(friends_ages["Jene"])

print("############################# 2nd instance ###################")

friends_ages = [
    {"name" : "Rolf", "Age": 30},
    {"name" : "Adam", "Age": 27},
    {"name" : "Jene", "Age": 24}
]
for friend in friends_ages:
    print(f"{friend['name']}'s age is {friend['Age']}")

print("############################# 3rd instance ###################")    

friends_ages = {"Rolf" : 30, "Adam" : 27, "Jene" : 24}

for friend in friends_ages:
    print(f"{friend}'s age is {friends_ages[friend]}")

print("############################# 4th instance ###################") 

friends_ages = {"Rolf" : 30, "Adam" : 27, "Jene" : 24}

print(list(friends_ages.items()))

for friend, age in friends_ages.items():
    print(f"{friend}'s age is {age}")

print("############################# 5th instance ###################")

friends_ages = [30, 27, 24]
friends_name = ["Rolf", "Adam", "Jene"]

print(enumerate(friends_ages))
print(enumerate(friends_name))

print(list(enumerate(friends_ages)), list(enumerate(friends_name)))

print("############################# 6th instance ###################")

friends_name = ["Rolf", "Adam", "Jene", "Rolf", "Adam", "Jene", "Adam", "Jene", "Rolf"]

friends_dict = {friend:[] for friend in friends_name}

print(friends_dict)

for index, friend in enumerate(friends_name):
    friends_dict[friend].append(index)

print(friends_dict)

print("######Convert two lists into a dictionary#######")

fruits = ["apples", "oranges", "guava", "pear"]
colors = ["red", "orange", "pink", "green"]

fruit_colors = {}

for fruit, color in zip(fruits, colors):
    fruit_colors[fruit] = color

print(fruit_colors)

print("###########################Merge two Python dictionaries into one##########################")

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict_result= {**dict1, **dict2}

print(dict_result)

### Print the value of key ‘history’ from the below dict

sampleDict = {"class": {"student": {"name": "Mike","marks": { "physics": 70,"history": 80}}}}

print(sampleDict["class"]["student"]["marks"]["history"])


#### Initialize dictionary with default values

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

resultant_dict = dict.fromkeys(employees,defaults)

print(resultant_dict)


############# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

resultant_dict = {}

for k in keys:
    resultant_dict.update({k:sample_dict[k]}) 

print(resultant_dict)

############# Delete a list of keys from a dictionary.

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

for k in keys:
    sample_dict.pop(k)

print(sample_dict)


###################Write a program to rename a key city to a location in the following dictionary.

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

keys = sample_dict.key()

for key in keys:
    if key == "city":
        key = ""