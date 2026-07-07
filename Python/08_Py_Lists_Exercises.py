"""
=====================================================
Lesson 010 - Lists
Exercise 001 - Storing Multiple Values
=====================================================

Objective:
Learn how to create, access, add to, remove from, and count items in a list.

Instructions:
- Read each section.
- Predict what will happen BEFORE running the code.
- Run the code in the terminal.
- Answer the questions in your own words.
"""


# =====================================================
# Exercise 1 - Create a List
# =====================================================

print("Exercise 1")

books = ["The Hobbit", "Dune", "The Alchemist"]

print(books)

# Questions:
#
# 1. What did the program print?
#    ['The Hobbit', 'Dune', 'The Alchemist']
#
# 2. What values are stored in the list?
#    "The Hobbit", "Dune", "The Alchemist"
#
# 3. Why is a list useful here?
#    It lets us store multiple books in a single variable.

# =====================================================
# Exercise 2 - Access Items by Index
# =====================================================

print("Exercise 2")

books = ["The Hobbit", "Dune", "The Alchemist"]

print(books[0])
print(books[1])
print(books[2])

# Questions:
#
# 1. What did books[0] print?
#    The Hobbit
#
# 2. What did books[1] print?
#    Dune
#
# 3. What did books[2] print?
#    The Alchemist
#
# 4. What does this show about list indexes?
#    They start at 0, and can be used to return any item in the list.

# =====================================================
# Exercise 3 - Add an Item
# =====================================================

print("Exercise 3")

books = ["The Hobbit", "Dune"]

books.append("The Alchemist")

print(books)

# Questions:
#
# 1. What did append() do?
#    Added "The Alchemist" to the end of the list.
#
# 2. Where was the new book added?
#    To the end of the list.
#
# 3. Did append() create a new list or change the existing list?
#    It changed the existing list.

# =====================================================
# Exercise 4 - Count Items
# =====================================================

print("Exercise 4")

books = ["The Hobbit", "Dune", "The Alchemist"]

book_count = len(books)

print(book_count)

# Questions:
#
# 1. What did len(books) return?
#    3
#
# 2. Why is len() useful?
#    It tells you how many items are in a list.
#    
# 3. How could this help the Library project?
#    We could use it to count the items in different lists such as, books in the library, books at checkout, or, users signed up.

# =====================================================
# Exercise 5 - Remove an Item
# =====================================================

print("Exercise 5")

books = ["The Hobbit", "Dune", "The Alchemist"]

books.remove("Dune")

print(books)

# Questions:
#
# 1. What did remove() do?
#    Removed an item from the list.
#
# 2. Which item was removed?
#    "Dune"
#
# 3. What would happen if you tried to remove a book that was not in the list?
#    You get a valueError.

# =====================================================
# Exercise 6 - Empty List
# =====================================================

print("Exercise 6")

books = []

books.append("The Hobbit")
books.append("Dune")

print(books)
print(len(books))

# Questions:
#
# 1. What was stored in books at the beginning?
#    An empty list.
#
# 2. What did the list contain after append() was used twice?
#    ['The Hobbit', 'Dune']
#
# 3. Why might starting with an empty list be useful?
#    It lets the list be created dynamically rather than hardcoded.

# =====================================================
# Exercise 7 - List Index Error
# =====================================================

print("Exercise 7")

books = ["The Hobbit", "Dune", "The Alchemist"]

print(books[3])

# Questions:
#
# 1. What error happened?
#    IndexError
#
# 2. Why did the error happen?
#    Because there is no index 3.
#
# 3. What is the highest valid index in this list?
#    2

# =====================================================
# Reflection
# =====================================================

# Key Takeaways:
#
# - A list stores multiple values in one variable.
# - Lists are ordered.
# - List indexes start at 0.
# - Use append() to add an item.
# - Use len() to count items.
# - Use remove() to remove an item.
# - Accessing an index that does not exist causes an error.


# Questions I still have:
#
#
#