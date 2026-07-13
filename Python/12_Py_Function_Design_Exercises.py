"""
=====================================================
Lesson 015 - Function Design
Exercise 001 - One Function One Job
=====================================================

Objective:
Practice identifying clear function responsibilities and separating logic into small focused functions.

Instructions:
- Read each section.
- Predict what will happen BEFORE running the code.
- Run the code in the terminal.
- Answer the questions in your own words.
"""


# =====================================================
# Exercise 1 - Clear Function Responsibility
# =====================================================

print("Exercise 1")

def show_message():
    print("Hello.")

show_message()

# Questions:
#
# 1. What is this function responsible for?
#    Displaying a message.
#
# 2. Is this function doing one job or many jobs?
#    One job.
#
# 3. Why is the name show_message clear?
#    It states a clear action.
#


# =====================================================
# Exercise 2 - Function Name Matches Action
# =====================================================

print("Exercise 2")

def greet_reader(name):
    print(f"Hello {name}.")

greet_reader("Anthony")

# Questions:
#
# 1. What action does greet_reader perform?
#    greet_reader displays a message using the text passed when the function is called. 
#   
# 2. What information does the function need?
#    A name.
#
# 3. Why is name a good parameter here?
#    A name is what is needed for the display message to make sense.
#


# =====================================================
# Exercise 3 - Display Function
# =====================================================

print("Exercise 3")

def display_books(book_list):
    for book in book_list:
        print(book)

books = ["The Alchemist", "Dune", "The Hobbit"]

display_books(books)

# Questions:
#
# 1. What is display_books responsible for?
#    Display all books in a list books.
#
# 2. What argument was passed into display_books?
#    books was the argument passed in to display_boooks().
#
# 3. Why does this function use print instead of return?
#    It only needs to display information. It does not need to return a value.
#


# =====================================================
# Exercise 4 - Formatting Function
# =====================================================

print("Exercise 4")

def format_name(name):
    return name.strip().title()

reader_name = format_name(" anthony ")

print(reader_name)

# Questions:
#
# 1. What is format_name responsible for?
#    formatting a name.
#
# 2. Why does this function use return instead of print?
#    We want to send data back when the function is called.
#
# 3. What value was stored in reader_name?
#    "Anthony"
#


# =====================================================
# Exercise 5 - Too Many Responsibilities
# =====================================================

print("Exercise 5")

def handle_reader():
    name = " anthony "
    formatted_name = name.strip().title()
    print(f"Hello {formatted_name}.")

handle_reader()

# Questions:
#
# 1. What jobs does handle_reader perform?
#    Stores the readers name, formats the readers name, displays the readers name.
#
# 2. Why might this function become harder to change later?
#    because name is built-in to the code block instead of being passed as a parameter.
#
# 3. How could this be split into smaller functions?
#    format_name should clean the name.
#    greet_reader should display the greeting.
#


# =====================================================
# Exercise 6 - Split Responsibilities
# =====================================================

print("Exercise 6")

def format_name(name):
    return name.strip().title()

def greet_reader(name):
    print(f"Hello {name}.")

reader_name = " anthony "
reader_name = format_name(reader_name)
greet_reader(reader_name)

# Questions:
#
# 1. What is format_name responsible for?
#    Formatting the readers name.
#
# 2. What is greet_reader responsible for?
#    Displaying a greeting to the reader.
#
# 3. Why is this design clearer than handle_reader?
#    Each function has one responsibility.
#


# =====================================================
# Exercise 7 - Display Book Records
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
        "checked_out": True
    },
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "checked_out": False
    }
]

def display_books(book_list):
    for book in book_list:
        print(f"{book['title']} by {book['author']}")

display_books(books)

# Questions:
#
# 1. What is display_books responsible for in this example?
#    Displaying the book title and author.
#
# 2. What does book_list refer to inside the function?
#    A list of dictionaries.
#
# 3. Why is display_books a better name than handle_books?
#    It describes a single action.
#


# =====================================================
# Exercise 8 - Return a Boolean
# =====================================================

print("Exercise 8")

def is_available(book):
    return not book["checked_out"]

book = {
    "title": "Dune",
    "author": "Frank Herbert",
    "checked_out": False
}

available = is_available(book)

print(available)

# Questions:
#
# 1. What is is_available responsible for?
#    is_available is responsible for checking whether a book is available and returning True or False.
#
# 2. Why does this function return a value?
#    That value is used later in the "available" variable as a boolean.
#
# 3. What value did available store?
#    True
#


# =====================================================
# Reflection
# =====================================================

# Key Takeaways:
#
# - A good function usually has one clear responsibility.
# - A function name should describe the action being performed.
# - A function should receive needed information through parameters.
# - Use print when the function's job is to display output.
# - Use return when the function's job is to produce a value needed later.
# - Small focused functions are easier to read, change, test, and reuse.


# Questions I still have:
#
#
#