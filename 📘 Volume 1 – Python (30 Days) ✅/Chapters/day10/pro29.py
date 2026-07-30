# Program 5 – Favorite Movie

# Take a movie name.

# Print:

# First 5 characters
# Remaining characters

# Example:

# Movie : Bahubali

# First Part : Bahub
# Second Part : ali


movie_name = input("Enter your favorite movie name :")

print(f"First part : {movie_name[0:5]}\n"
      f"Second part : {movie_name[5:]}")