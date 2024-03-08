users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "jose123"),
    (3, "Jene", "jenifer123")
]

user_creds = {user[1]:user for user in users}

print(user_creds)

username = input("Enter a username: ")
password = input("Enter a password: ")

_, username, password = [user for users ]