movies_i_have_watched = {"Godfather", "Shawshank Redemption", "Life is Beautiful", "Jurassic Park"}
movies_i_have_watched_lower = {movie.lower() for movie in movies_i_have_watched}
nishants_watched_list = input("Enter the movie which Nishant has watched: ").lower()

if nishants_watched_list in movies_i_have_watched_lower:
    print(f"I have already watched {nishants_watched_list}")
else:
    print(f"I am yet to watch {nishants_watched_list}")

print("##############################2nd Exercise(magic number)#############################")

number = 7

user_input

