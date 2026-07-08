"""
=====================================================
Lesson 011 - Loops
Exercise 001 - Repeating Actions
=====================================================

Objective:
Learn how to repeat actions using for loops.

Instructions:
- Read each section.
- Predict what will happen BEFORE running the code.
- Run the code in the terminal.
- Answer the questions in your own words.
"""


# =====================================================
# Exercise 1 - Basic for Loop
# =====================================================

print("Exercise 1")

books = ["The Alchemist", "Dune", "The Hobbit"]

for book in books:
    print(book)

# Questions:
#
# 1. What did the program print?
#    Python printed each book on its own line.
#
# 2. How many times did the loop run?
#    3
#
# 3. What did book refer to each time through the loop?
#    An item in the books list.

# =====================================================
# Exercise 2 - Loop Variable
# =====================================================

print("Exercise 2")

names = ["Anthony", "Bob", "Sarah"]

for name in names:
    print(f"Hello {name}.")

# Questions:
#
# 1. What did the program print?
#    Hello Anthony
#    Hello Bob
#    Hello Sarah
#
# 2. What is the loop variable?
#    name is the loop variable. It refers to the current item in the names list during each loop pass.
#
# 3. What is the list?
#    A collection of names.

# =====================================================
# Exercise 3 - Indentation
# =====================================================

print("Exercise 3")

books = ["The Alchemist", "Dune", "The Hobbit"]

for book in books:
    print(book)

print("Done")

# Questions:
#
# 1. Which line repeated?
#    print(book)
#
# 2. Which line printed only once?
#    print("Done")
#
# 3. Why did "Done" only print once?
#    It was outside the loop.

# =====================================================
# Exercise 4 - Loop Through Updated List
# =====================================================

print("Exercise 4")

books = ["The Alchemist", "Dune"]

books.append("The Hobbit")
books.append("1984")

for book in books:
    print(book)

# Questions:
#
# 1. Which books printed?
#    All books including the appended ones.
#
# 2. Why did the new books print too?
#    They were added to the list before the loop ran.
#
# 3. Why is this better than printing by index?
#    Printing the items with a loop is better than printing by index because
#    a loop will print the full list even after adding items.

# =====================================================
# Exercise 5 - Count While Looping
# =====================================================

print("Exercise 5")

books = ["The Alchemist", "Dune", "The Hobbit"]

book_count = 0

for book in books:
    book_count = book_count + 1
    print(book)

print(book_count)

# Questions:
#
# 1. What did book_count start as?
#    book_count started as integer 0.
#
# 2. What happened to book_count each time through the loop?
#    book_count increased its value by 1 each time the loop ran. 
#
# 3. What did book_count print at the end?
#    book_count printed 3.

# =====================================================
# Exercise 6 - Loop with Condition
# =====================================================

print("Exercise 6")

books = ["The Alchemist", "Dune", "The Hobbit"]

for book in books:
    if book == "Dune":
        print("Found Dune.")

# Questions:
#
# 1. What printed?
#    "Found Dune" was printed.
#
# 2. Why did it only print for Dune?
#    Python printed "Found Dune." only when book was equal to "Dune".
#    For the other books, the condition was False, so Python skipped the indented block and moved on.
#
# 3. How could this help the Library project?
#    This loop approach can be used to make a search feature in the library project.

# =====================================================
# Exercise 7 - Empty List
# =====================================================

print("Exercise 7")

books = []

for book in books:
    print(book)

print("Finished checking books.")

# Questions:
#
# 1. Did the loop print any books?
#    The loop did not print any books.
#
# 2. Why or why not?
#    The loop did not print any books because the books list is empty.
#
# 3. What printed after the loop?
#    Python printed "Finished checking books." after the loop.

# =====================================================
# Reflection
# =====================================================

# Key Takeaways:
#
# - A loop repeats a block of code.
# - A for loop runs once for each item in a collection.
# - The loop variable refers to the current item.
# - Indentation controls what repeats.
# - Loops work even when the list changes size.
# - A loop over an empty list runs zero times.


# Questions I still have:
#
#
#