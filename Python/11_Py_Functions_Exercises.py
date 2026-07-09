"""
=====================================================
Lesson 014 - Functions
Exercise 001 - Named Actions
=====================================================

Objective:
Learn how to define functions, call functions, and pass values into functions.

Instructions:
- Read each section.
- Predict what will happen BEFORE running the code.
- Run the code in the terminal.
- Answer the questions in your own words.
"""


# =====================================================
# Exercise 1 - Define a Function
# =====================================================

print("Exercise 1")

def show_message():
    print("Hello from inside the function.")

show_message()

# Questions:
#
# 1. What did the program print?
#    "Hello from inside the function."
#
# 2. Which line defined the function?
#    def show_message():
#
# 3. Which line called the function?
#    show_message()
#


# =====================================================
# Exercise 2 - Function Does Not Run Until Called
# =====================================================

print("Exercise 2")

def show_warning():
    print("This warning is inside the function.")

print("Before function call.")
show_warning()
print("After function call.")

# Questions:
#
# 1. What printed first?
#    "Before function call."
#
# 2. When did the warning message print?
#    The warning message was the second message to print.
#
# 3. Why did the function body not run before the function call?
#    Because the function must be called before it runs the body.
#


# =====================================================
# Exercise 3 - Forgetting to Call a Function
# =====================================================

print("Exercise 3")

def show_library_name():
    print("Bailey's Books and Bargains")

print("The function has been defined.")

# Questions:
#
# 1. Did the library name print?
#    It did not.
#
# 2. Why or why not?
#    The function was never called
#
# 3. What line would you add to call the function?
#    show_library_name()
#


# =====================================================
# Exercise 4 - Function with One Parameter
# =====================================================

print("Exercise 4")

def greet_reader(name):
    print(f"Hello {name}.")

greet_reader("Anthony")

# Questions:
#
# 1. What did the program print?
#    "Hello Anthony."
#
# 2. What is the parameter?
#    name
#
# 3. What is the argument?
#    "Anthony"
#


# =====================================================
# Exercise 5 - Call the Same Function with Different Arguments
# =====================================================

print("Exercise 5")

def greet_reader_2(name):
    print(f"Hello {name}.")

greet_reader_2("Anthony")
greet_reader_2("Sarah")
greet_reader_2("Bob")

# Questions:
#
# 1. How many times did the function run?
#    3
#
# 2. What changed each time the function ran?
#    The argument.
#
# 3. Why is this better than writing three separate print statements?
#    We only need to update the logic inside the function.
#


# =====================================================
# Exercise 6 - Function with Project Data
# =====================================================

print("Exercise 6")

library_name = "Bailey's Books and Bargains"

def show_welcome_message(name):
    print(f"Welcome to {name}.")

show_welcome_message(library_name)

# Questions:
#
# 1. What did the program print?
#    "Welcome to Bailey's Books and Bargains."
#
# 2. What value was passed into the function?
#    The value stored in library_name.
#
# 3. What did the parameter name refer to inside the function?
#    The name to be used in the welcome message.
#


# =====================================================
# Exercise 7 - Function with a List
# =====================================================

print("Exercise 7")

books = ["The Alchemist", "Dune", "The Hobbit"]

def display_books(book_list):
    for book in book_list:
        print(book)

display_books(books)

# Questions:
#
# 1. What did the program print?
#    The full book list, newline separated.
#
# 2. What is the parameter?
#    book_list
#
# 3. What argument was passed into the function?
#    books
#
# 4. What did the loop variable book refer to each time through the loop?
#    The current book title in the list.
#


# =====================================================
# Exercise 8 - Function with a List of Dictionaries
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

def display_book_titles(book_list):
    for book in book_list:
        print(book["title"])

display_book_titles(books)

# Questions:
#
# 1. What did the program print?
#    The title of each book, newline separated.
#
# 2. What did book_list refer to inside the function?
#    The list of dictionaries containing title, author, and checked_out status for each book.
#
# 3. What did book refer to each time through the loop?
#    The current dictionary containing book information.
#
# 4. What did book["title"] access?
#    The title of each book.
#


# =====================================================
# Reflection
# =====================================================

# Key Takeaways:
#
# - A function is a reusable named block of code.
# - A function is defined with def.
# - A function body must be indented.
# - A function does not run until it is called.
# - Parentheses are required when calling a function.
# - A parameter is a placeholder in the function definition.
# - An argument is the actual value passed into the function call.
# - Functions can receive strings, numbers, lists, dictionaries, or other values.
# - Functions help organize repeated actions.


# Questions I still have:
#
#
#