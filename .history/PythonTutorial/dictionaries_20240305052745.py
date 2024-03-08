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

for friend in friends_ages