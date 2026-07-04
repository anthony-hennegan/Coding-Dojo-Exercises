"""
=====================================================
Conditionals
if / elif / else
=====================================================

Objective:
Learn how Python makes decisions using conditionals.

Instructions:
- Read each section.
- Predict what will happen BEFORE running the code.
- Run the code in the terminal.
- Answer the questions in your own words.
"""


# =====================================================
# Exercise 1 - Basic if Statement
# =====================================================

# Task:
# Check whether the user typed "yes".

answer = input("Would you like to continue? ")

if answer == "yes":
    print("Continuing...")

# Questions:
#
# 1. What happens if you type yes?
#   Output will be "Continuing..."
# 2. What happens if you type no?
#   The program will stop
# 3. Why does Python only print the message sometimes?
#   There is nothing handling answers that are not "yes"


# =====================================================
# Exercise 2 - if / else
# =====================================================

# Task:
# Give one response for yes and another response for everything else.

answer = input("Would you like to view the book selection? ")

if answer == "yes":
    print("Here are our books.")
else:
    print("No problem. Have a nice day.")

# Questions:
#
# 1. What happens if you type yes?
#   Output will be "Here are our books."
# 2. What happens if you type no?
#   Output will be "No problem. Have a nice day."
# 3. What happens if you type banana?
#   Output will be "No problem. Have a nice day."
# 4. Why does else catch everything that is not yes?
#   Else handles all conditions that are not equal to "yes"


# =====================================================
# Exercise 3 - if / elif / else
# =====================================================

# Task:
# Handle yes, no, and unexpected responses separately.

answer = input("Would you like to check out a book? ")

if answer == "yes":
    print("Great. Let's find you a book.")
elif answer == "no":
    print("No problem. Maybe next time.")
else:
    print("Please type yes or no.")

# Questions:
#
# 1. What happens if you type yes?
#   Output will be "Great. Let's find you a book."
# 2. What happens if you type no?
#   Output will be "No problem. Maybe next time."
# 3. What happens if you type something else?
#   Output will be "Please type yes or no."
# 4. Why is elif useful here?
#   It lets you have unique responses for multiple conditions.


# =====================================================
# Exercise 4 - Case Sensitivity
# =====================================================

# Task:
# Observe how Python compares strings exactly.

answer = input("Type yes: ")

if answer == "yes":
    print("Matched yes.")
else:
    print("Did not match yes.")

# Try typing:
# yes
# Yes
# YES
# yes with a space after it

# Questions:
#
# 1. Which inputs matched?
#   "yes"
# 2. Which inputs did not match?
#   All but "yes"
# 3. What does this show about string comparison?
#   They must be exact.


# =====================================================
# Exercise 5 - Boolean Variable
# =====================================================

# Task:
# Use a boolean variable in a conditional.

is_open = True

if is_open:
    print("The library is open.")
else:
    print("The library is closed.")

# Questions:
#
# 1. Why does this condition not need == True?
#   Because is_open is already a boolean value. Python can evaluate it directly.

# 2. What happens if you change is_open to False?
#   Python skips the if block and runs the else block.

# 3. What does this show about boolean values?
#    Boolean values work naturally as conditions because they are already True or False.


# =====================================================
# Reflection
# =====================================================

# Key Takeaways:
#
# - Conditionals allow a program to choose which code runs.
# - if checks a condition.
# - elif checks another condition if the previous condition was false.
# - else runs when none of the previous conditions were true.
# - Python only runs the block that matches the condition.
# - String comparisons are exact.
# - Indentation defines which statements belong to each block.


# Questions I still have:
#
#
#