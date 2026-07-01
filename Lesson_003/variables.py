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
print("Exercise 1")

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
print("")
print("Exercise 2")

# Task:
# Replace the three print statements with one print statement.

print(name, age, favorite_language)

# Questions
#
# What changed?
# All three values are printed on the same line.
#
# Why are the values printed on one line?
# Because a single print() call prints all of its arguments before
# appending one newline character.
#
# What does print() append by default?
# A newline character (\n).


# =====================================================
# Exercise 3 - Reassign a Variable
# =====================================================
print("")
print("Exercise 3")

# Prediction:
# What do you think the output will be?
# Anthony
# Bob
#
# Why?
# The first print() executes before name is changed to "Bob".
# After the reassignment, name refers to "Bob", so the second print()
# outputs Bob.

name = "Anthony"

print(name)

name = "Bob"

print(name)


# =====================================================
# Exercise 4 - Multiple Reassignments
# =====================================================
print("")
print("Exercise 4")

# Prediction:
#
# What will the program print?
#   Anthony
#   Bob
#   Charlie
#
# Explain WHY.
# Python executes one statement at a time from top to bottom.
# Each print() uses the value that the variable refers to at the
# moment that statement executes.

name = "Anthony"

print(name)

name = "Bob"

print(name)

name = "Charlie"

print(name)


# =====================================================
# Exercise 5 - Independent Variables
# =====================================================
print("")
print("Exercise 5")

# Prediction:
#
# What will this print?
#   Anthony
#   34
#   Anthony
#   35
# Why doesn't changing age affect name?
#   Because the name and age variables are independent of each other. 
#   Changing one does not affect the other.

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

# Key Takeaways
#
# • Python executes statements from top to bottom.
# • Variables refer to values.
# • Variables can be reassigned to different values.
# • Each statement uses the current state of the program when it executes.
# • print() appends a newline character (\n) by default.
