"""
=====================================================
Lesson 003 - Python Fundamentals
Exercise 001 - Variables
=====================================================

Objective:
Learn how variables store values and how Python
executes code from top to bottom.

Instructions:
- Read each section.
- Predict what will happen BEFORE running the code.
- Run the code.
- Answer the questions in your own words.
"""

# =====================================================
# Exercise 1 - Create Variables
# =====================================================

# Task:
# Create three variables and print each one.

name = "Anthony"
age = 34
favorite_language = "Python"

print(name)
print(age)
print(favorite_language)

# Questions
#
# 1. What does each variable refer to?
#
#    name refers to the string "Anthony".
#    age refers to the integer 34.
#    favorite_language refers to the string "Python".
# 
# 2. What does each print() statement output?
#
#    Anthony
#    34
#    Python
#
# 3. Why does each value appear on its own line?
#
#    Because print() appends a newline character (\n) after printing by default.


# =====================================================
# Exercise 2 - Print Multiple Values
# =====================================================

# Task:
# Replace the three print statements with one print statement.

print(name, age, favorite_language)

# Questions
#
# 1. What changed?
#
#    All three values are printed on the same line.
#
# 2. Why are the values printed on one line?
#
#    Because a single print() call prints all of its arguments before
#    appending one newline character.
#
# 3. What does print() append by default?
#
#    A newline character (\n).


# =====================================================
# Exercise 3 - Reassign a Variable
# =====================================================

# Prediction:
#
# Before running this code...
#
# What do you think the output will be?
#
#   Anthony
#   Bob
#
# Why?
#   Python executes from top to bottom.

name = "Anthony"

print(name)

name = "Bob"

print(name)


# =====================================================
# Exercise 4 - Multiple Reassignments
# =====================================================

# Prediction:
#
# What will the program print?
#
# Explain WHY.

name = "Anthony"

print(name)

name = "Bob"

print(name)

name = "Charlie"

print(name)


# =====================================================
# Exercise 5 - Independent Variables
# =====================================================

# Prediction:
#
# What will this print?
#
# Why doesn't changing age affect name?

name = "Anthony"
age = 34

print(name)
print(age)

age = 35

print(name)
print(age)


# =====================================================
# Reflection
# =====================================================

# What surprised you?
#
#
#
# What was confusing?
#
#
#
# What did you learn?
#
#
#
# Questions to ask next session:
#
#
#
