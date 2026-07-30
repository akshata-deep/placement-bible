# Question 8 — Deadly High (Placement Level)
# 📌 Problem: Library Book Management System

# Create a menu-driven program.

# Menu:

# ===== Library Menu =====
# 1. View Books
# 2. Check Book Availability
# 3. Exit

# Requirements:

# Store at least 6 book names in a list.
# View Books: Display all books with serial numbers.
# Check Book Availability: Ask the user for a book name. If it exists, print "Book Available", otherwise print "Book Not Available".
# Continue showing the menu until the user chooses Exit.
# Use lists, loops, in operator, and functions wherever appropriate.





books = ["Ganita Prakash","Curiosity for Science","Exploring Society","India","Beyond","Ncrt" ]
print("===== Library Menu =====\n"
      "1. View Books\n"
      "2. Check Book Availability\n"
      "3. Exit\n")

while True :
    option = int(input("Enter the option : "))
    if option == 1:
        print(books)
    elif option == 2:
        checking = input("Enter the book name :")
        if checking in books:
            print("Found")
        else:
            print("Not Found")
    else:
        break