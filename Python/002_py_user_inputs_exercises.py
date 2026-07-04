"""
=====================================================
User Input
input()
=====================================================

Objective:
Learn how Python receives information from the user
with input() and stores that information in variables.

Instructions:
- Read each section.
- Predict what will happen BEFORE running the code.
- Run the code in the terminal, not the Output panel.
- Answer the questions in your own words.
"""


# =====================================================
# Exercise 1 - Basic User Input
# =====================================================

# Task:
# Ask the user for their name and print it back.

# Prediction:
# 1. What will Python display?
#   It will show "What is your name?"

# 2. What happens after the user types a response?
#   Python will store the reponse, then print the response.
  
# 3. What value will the variable refer to?
#   The users response.

name = input("What is your name? ")

print(name)

# Questions:
#
# 1. What did input() display?
#   "What is your name?"

# 2. What did you type?
#   "Tony"

# 3. What did print(name) display?
#   "Tony"

# 4. What data type do you think name is?
#   A string


# =====================================================
# Exercise 2 - Input Stored in a Variable
# =====================================================

# Task:
# Ask the user for their favorite book.

favorite_book = input("What is your favorite book? ")

print("Your favorite book is:")
print(favorite_book)

# Questions:
#
# 1. What value did favorite_book refer to?
#   The user input: "The Alchemist"
# 2. Why could Python print favorite_book later?
#   Because the user input became the value, and print is executed after
#   the input statement.
# 3. What does this show about variables?
#   Variable store data that can be wriiten directly or as a user input.


# =====================================================
# Exercise 3 - Multiple Inputs
# =====================================================

# Task:
# Ask for multiple pieces of information.

reader_name = input("Reader name: ")
book_title = input("Book title: ")
author_name = input("Author name: ")

print("Reader:")
print(reader_name)

print("Book:")
print(book_title)

print("Author:")
print(author_name)

# Questions:
#
# 1. How many times did the program pause for input?
#   3
# 2. Which variable stored the reader's name?
#   reader_name
# 3. Which variable stored the book title?
#   book_title
# 4. Which variable stored the author's name?
#   author_name

# =====================================================
# Exercise 4 - Input Is Always a String
# =====================================================

# Task:
# Ask for a number and print it.

book_count = input("How many books do you own? ")

print(book_count)

# Questions:
#
# 1. If you typed 20, did Python store it as 20 or "20"?
#   "20"
# 2. What data type does input() return?
#   str
# 3. Why might this matter later if we want to do math?
#   We would have to convert the data type

# =====================================================
# Exercise 5 - Build a Message from Input
# =====================================================

# Task:
# Ask for a name and book, then print a simple message.

user_name = input("What is your name? ")
requested_book = input("What book are you looking for? ")

print("Hello", user_name)
print("You are looking for:", requested_book)

# Questions:
#
# 1. Which values came from the user?
#   user_name, requested_book
# 2. Which values were written directly in the code?
#   Hello, You are looking for:
# 3. How did input() make the program interactive?
#   It let the user type the name and book title

# =====================================================
# Reflection
# =====================================================

# Key Takeaways:
#
# - input() displays a prompt.
# - input() pauses the program.
# - The user types a response and presses Enter.
# - input() returns the response as a string.
# - The returned value can be stored in a variable.
# - User input makes a program interactive.


# Questions I still have:
#
#
#