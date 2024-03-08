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

student_score = {"Adam": 70, "Rita": 78, "Roger": 85}

student_major = {"Adam": "Maths", "Rita": "Economics", "Roger": "Life Science"}

student_major_score = {}

for student, major, score in zip()