# users = [
#     (0, "Bob", "password"),
#     (1, "Rolf", "bob123"),
#     (2, "Jose", "jose123"),
#     (3, "Jene", "jenifer123")
# ]

# user_creds = {user[1]:user for user in users}

# print(user_creds)

# username = input("Enter a username: ")
# password = input("Enter a password: ")

# print(user_creds[username])

# _, user, passw = user_creds[username]

# if password == passw:
#     print("successful login!")
# else:
#     print("failed login")


# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
student = {'name': 'Jose', 'school': 'Computing', 'grades': (66, 77, 88)}

# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.
# def average_grade(data):
#     grades =   list(student['grades'])
#     return sum(grades) / len(grades)

# print(average_grade(student))

# Implement the function below
# Given a list of students (a list of dictionaries), calculate the average grade received on an exam, for the entire class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list

student_list = [
    {"name": "Alice", "major": "Computer Science", "grade": 90},
    {"name": "Bob", "major": "Mathematics", "grade": 85},
    {"name": "Charlie", "major": "Physics", "grade": 88}
]

grades_list = []
def average_grade_all_students(student_list):
    total = 0
    count = 0
    
    
    for student in student_list:
        grades_list = grades_list.append(student["grades"])# Implement here
    total = sum(grades_list)
    count = lengt

    return total / count