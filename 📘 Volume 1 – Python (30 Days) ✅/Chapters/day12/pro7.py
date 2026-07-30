# Username Cleaner

# Take a username with extra spaces (for example: " akshata123 ").

# Print:

# Original username
# Clean username using strip()
# Username in uppercase
# Length before cleaning
# Length after cleaning


username = "             akshata    "
clean = username.strip()
print(f"original username : {username}\n"
      f"clean username : {clean}\n"
      f"uppercase : {clean.upper()}\n"
      f"Length before cleaning : {len(username)}\n"
      f"Length after cleaning :{len(clean)}\n")