"""
=====================================================
Lesson 012 - Dictionaries
Exercise 001 - Grouping Related Data
=====================================================

Objective:
Learn how to use dictionaries to store multiple pieces of related information in one place.

Instructions:
- Read each section.
- Predict what will happen BEFORE running the code.
- Run the code in the terminal.
- Answer the questions in your own words.
"""


# =====================================================
# Exercise 1 - Basic Dictionary
# =====================================================

print("Exercise 1")

book = {
    "title": "Dune",
    "author": "Frank Herbert",
    "checked_out": False
}

print(book)

# Questions:
#
# 1. What did the program print?
#    {'title': 'Dune', 'author': 'Frank Herbert', 'checked_out': False}
#
# 2. What kind of data structure is book?
#    The data structure for book is a dictionary.
#
# 3. Why is a dictionary useful here?
#    A dictionary for this scenario because it lets us group book information and store that data in one place.
#


# =====================================================
# Exercise 2 - Access Dictionary Values
# =====================================================

print("Exercise 2")

book = {
    "title": "Dune",
    "author": "Frank Herbert",
    "checked_out": False
}

print(book["title"])
print(book["author"])

# Questions:
#
# 1. What did the program print?
#    Dune
#    Frank Herbert
#
# 2. What does book["title"] access?
#    book["title"] accesses the value for the dict key "title" in the book variable.
#    "Dune"
#
# 3. What does book["author"] access?
#    book["author"] accesses the value for the dict key "author" in the book variable.
#    "Frank Herbert"
#


# =====================================================
# Exercise 3 - Update a Dictionary Value
# =====================================================

print("Exercise 3")

book = {
    "title": "Dune",
    "author": "Frank Herbert",
    "checked_out": False
}

print(book["checked_out"])

book["checked_out"] = True

print(book["checked_out"])

# Questions:
#
# 1. What did checked_out print before the update?
#    check_out printed False before the update.
#
# 2. What did checked_out print after the update?
#    check_out printed True after the update.
#
# 3. What line changed the value?
#    book["checked_out"] = True change the value of check_out.
#


# =====================================================
# Exercise 4 - Add a New Key
# =====================================================

print("Exercise 4")

book = {
    "title": "Dune",
    "author": "Frank Herbert",
    "checked_out": False
}

book["year"] = 1965

print(book)

# Questions:
#
# 1. What new key was added to the dictionary?
#    "year" was the new key added to the book dictionary.
#
# 2. What value was stored under that key?
#    1965 was the value stored under the "year" key.
#
# 3. Did Python allow us to add a new key after the dictionary was created?
#    Yes, Python allowed a new key to be added after the dictionary was created with this line of code:
#    book["year"] = 1965
#


# =====================================================
# Exercise 5 - List of Dictionaries
# =====================================================

print("Exercise 5")

books = [
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "checked_out": False
    },
    {
        "title": "Dune",
        "author": "Frank Herbert",
        "checked_out": False
    },
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "checked_out": False
    }
]

print(books)

# Questions:
#
# 1. What kind of data structure is books?
#    The data structure for variable books is a list of dictionaries.
#
# 2. What kind of data structure is each item inside books?
#    The data structure for each item inside books is a dictionary.
#
# 3. Why is this better than only storing book titles as strings?
#    Storing the books as a list of dictionaries is better than storing the books as list of title strings
#    becuase the dictionary let us store and manipulate multiple pieces of data for each book.
#


# =====================================================
# Exercise 6 - Loop Through a List of Dictionaries
# =====================================================

print("Exercise 6")

books = [
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "checked_out": False
    },
    {
        "title": "Dune",
        "author": "Frank Herbert",
        "checked_out": False
    },
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "checked_out": False
    }
]

for book in books:
    print(book["title"])

# Questions:
#
# 1. What did the program print?
#    The program printed the title for every book in the list on a new line.
#
# 2. What does book refer to each time through the loop?
#    book refers to the current dictionary running in the code block.
#
# 3. What does book["title"] access?
#    book["title"] accesses the dictionary key "title" for the current item. 
#


# =====================================================
# Exercise 7 - Print Book Details
# =====================================================

print("Exercise 7")

books = [
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "checked_out": False
    },
    {
        "title": "Dune",
        "author": "Frank Herbert",
        "checked_out": False
    },
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "checked_out": False
    }
]

for book in books:
    print(f"{book['title']} by {book['author']}")

# Questions:
#
# 1. What did the program print?
#    The program printed the book title by the authors name for every book on a new line.
#
# 2. Why did we use book["title"] and book["author"]?
#    We used book["title"] and book["author"] becasue their values are the book titles and author names for each book.
#
# 3. Why are single quotes used inside the f-string?
#    We single quotes inside f-strings because double quotes will close the f-string prematurely and single quotes are read
#    strings.
#


# =====================================================
# Exercise 8 - Check Book Status
# =====================================================

print("Exercise 8")

books = [
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "checked_out": False
    },
    {
        "title": "Dune",
        "author": "Frank Herbert",
        "checked_out": True
    },
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "checked_out": False
    }
]

for book in books:
    if book["checked_out"]:
        print(f"{book['title']} is checked out.")
    else:
        print(f"{book['title']} is available.")

# Questions:
#
# 1. Which book was checked out?
#    Dune was checked out.
#
# 2. Which books were available?
#    The Hobbit and The Alchemist were available.
#
# 3. How did Python decide which message to print?
#    Python decided what message to print by looping through each dict in the list of books and 
#    checking the check_out value for True or False.
#


# =====================================================
# Exercise 9 - Update One Book in the List
# =====================================================

print("Exercise 9")

books = [
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "checked_out": False
    },
    {
        "title": "Dune",
        "author": "Frank Herbert",
        "checked_out": False
    },
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "checked_out": False
    }
]

books[1]["checked_out"] = True

for book in books:
    if book["checked_out"]:
        print(f"{book['title']} is checked out.")
    else:
        print(f"{book['title']} is available.")

# Questions:
#
# 1. What does books[1] refer to?
#    books[1] refers to the second dictionary in the list.
#
# 2. What value was changed?
#    The checked_out value for the second dictionary was changed to True.
#
# 3. Why did only Dune show as checked out?
#    Dune showed as checked out because its checked_out status was changed to True
#


# =====================================================
# Reflection
# =====================================================

# Key Takeaways:
#
# - A dictionary stores data as key-value pairs.
# - A key is the name used to access a value.
# - A value is the data stored under a key.
# - Dictionaries are useful for grouping related data.
# - A list can store multiple dictionaries.
# - A loop can go through a list of dictionaries.
# - Dictionary values can be read, updated, and added.
# - books[1]["checked_out"] means:
#   go to the second item in the books list,
#   then access or update its checked_out value.


# Questions I still have:
#
#
#