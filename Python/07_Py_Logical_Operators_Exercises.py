"""
=====================================================
Lesson 009 - Logical Operators
Exercise 001 - and, or, not
=====================================================

Objective:
Learn how to combine and reverse conditions using logical operators.

Instructions:
- Read each section.
- Predict what will happen BEFORE running the code.
- Run the code in the terminal.
- Answer the questions in your own words.
"""


# =====================================================
# Exercise 1 - and
# =====================================================

print("Exercise 1")

is_open = True
requested_books = 2
checkout_limit = 3

print(is_open and requested_books <= checkout_limit)

# Questions:
#
# 1. What did the program print?
#    True
#
# 2. Why was the result True or False?
#    The result was True because is_open was True and requested_books <= checkout_limit was also True.
#
# 3. What must be true for an and condition to be True?
#    Both conditions must be true.

# =====================================================
# Exercise 2 - and with One False Condition
# =====================================================

print("Exercise 2")

is_open = False
requested_books = 2
checkout_limit = 3

print(is_open and requested_books <= checkout_limit)

# Questions:
#
# 1. What did the program print?
#    False
#
# 2. Which condition was False?
#    is_open was false.
#
# 3. Why did the whole expression become False?
#    Because the and operator requires both conditions be true to return a true result.

# =====================================================
# Exercise 3 - or
# =====================================================

print("Exercise 3")

answer = "y"

print(answer == "yes" or answer == "y")

# Questions:
#
# 1. What did the program print?
#    True
# 2. Which part of the condition was True?
#    answer == "y"
#
# 3. What must be true for an or condition to be True?
#    Atleast one of the expressions must be True.

# =====================================================
# Exercise 4 - or with Both False
# =====================================================

print("Exercise 4")

answer = "maybe"

print(answer == "yes" or answer == "y")

# Questions:
#
# 1. What did the program print?
#    False
# 2. Why was the result False?
#    Neither conditions were true.
#
# 3. When would or be useful in the Library project?
#    or is useful when we want to accept more than one valid input like "yes" or "y".

# =====================================================
# Exercise 5 - not
# =====================================================

print("Exercise 5")

is_open = False

print(not is_open)

# Questions:
#
# 1. What did the program print?
#    True
#
# 2. What did not do to the value?
#    Reversed the boolean result.
#
# 3. When would not be useful?
#    not is useful when we want to run code when something is false like when the library is not open.

# =====================================================
# Exercise 6 - not in a Conditional
# =====================================================

print("Exercise 6")

is_open = False

if not is_open:
    print("The library is closed.")
else:
    print("The library is open.")

# Questions:
#
# 1. Which message printed?
#    "The library is closed."
#
# 2. Why did that message print?
#    is_open is false.
#
# 3. What does if not is_open mean?
#    If is_open == False.

# =====================================================
# Exercise 7 - Combine User Input with or
# =====================================================

print("Exercise 7")

answer = input("Would you like to view our book selection? ")
answer = answer.strip().lower()

if answer == "yes" or answer == "y":
    print("Showing books.")
elif answer == "no" or answer == "n":
    print("No worries. Have a nice day.")
else:
    print("Please type yes or no.")

# Try typing:
# yes
# y
# no
# n
# maybe

# Questions:
#
# 1. What happened when you typed yes?
#    The program returned "Showing books.".
#
# 2. What happened when you typed y?
#    The program returned "Showing books.".
#
# 3. What happened when you typed no?
#    The program returned "No worries. Have a nice day.".
#
# 4. What happened when you typed n?
#    The program returned "No worries. Have a nice day.".
#
# 5. Why is or useful here?
#    or lets multiple accepted answers run the same code block.

# =====================================================
# Exercise 8 - Combine Conditions with and
# =====================================================

print("Exercise 8")

is_open = True
checkout_limit = 3

requested_books = input("How many books would you like to check out? ")
requested_books = int(requested_books)

if is_open and requested_books <= checkout_limit:
    print("Checkout approved.")
else:
    print("Checkout is not available.")

# Try typing:
# 2
# 3
# 4

# Questions:
#
# 1. What happened when you typed 2?
#    The program returned "Checkout approved.".
#
# 2. What happened when you typed 3?
#    The program returned "Checkout approved.".
#
# 3. What happened when you typed 4?
#    The program returned "Checkout is not available.".
#
# 4. Why is and useful here?
#    It makes sure multiple conditons are true before executing the specified code block.


# =====================================================
# Reflection
# =====================================================

# Key Takeaways:
#
# - and requires both conditions to be True.
# - or requires at least one condition to be True.
# - not reverses a boolean value.
# - Logical operators are often combined with comparison operators.
# - Logical operators help programs make decisions using multiple conditions.


# Questions I still have:
#
#
#