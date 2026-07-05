"""
=====================================================
Lesson 006 - String Methods
Exercise 001 - Cleaning and Normalizing Text
=====================================================

Objective:
Learn how to use string methods to clean and normalize user input.

Instructions:
- Read each section.
- Predict what will happen BEFORE running the code.
- Run the code in the terminal.
- Answer the questions in your own words.
"""


# =====================================================
# Exercise 1 - lower()
# =====================================================
print("Exercise 1")
# Task:
# Convert text to lowercase.

answer = "YES"

print(answer.lower())

# Questions:
#
# 1. What did the program print?
#   yes
#
# 2. Did the original answer variable change?
#   No. lower() returned a new lowercase string, but the result was not stored.
#
# 3. What does lower() do?
#   Makes all strings lower case.


# =====================================================
# Exercise 2 - upper()
# =====================================================
print("Exercise 2")
# Task:
# Convert text to uppercase.

answer = "yes"

print(answer.upper())

# Questions:
#
# 1. What did the program print?
#   YES
#
# 2. What does upper() do?
#   Make all strings upper case.
#
# 3. When might uppercase text be useful?
#   Emphasis on an important word or phrase.
#   Writing a page or section heading.
#   Validating input response.

# =====================================================
# Exercise 3 - strip()
# =====================================================
print("Exercise 3")
# Task:
# Remove spaces from the beginning and end of a string.

answer = " yes or no "

print(answer.strip())

# Questions:
#
# 1. What did the program print?
#   "yes or no"
#
# 2. What spaces were removed?
#   The spaces at the start and end of the string.
#
# 3. Did strip() remove spaces from the middle of the string?
#   No


# =====================================================
# Exercise 4 - Chaining Methods
# =====================================================
print("Exercise 4")
# Task:
# Use more than one string method together.

answer = " YES or NO "

clean_answer = answer.strip().lower()

print(clean_answer)

# Questions:
#
# 1. What did the program print?
#   "yes or no"
#
# 2. Which method ran first?
#   .strip()
#
# 3. Which method ran second?
#   .lower()
#
# 4. Why is this useful for user input?
#   It lets us standardize the response to make validation more consistent.


# =====================================================
# Exercise 5 - Methods Return New Strings
# =====================================================
print("Exercise 5")
# Task:
# Observe that string methods return new strings.

answer = " YES "

answer.strip().lower()

print(answer)

# Questions:
#
# 1. What did the program print?
#   " YES "
#
# 2. Why did answer not change?
#   The result from cleaning answer was not stored.
#
# 3. How would you correctly store the cleaned value?
#   answer = answer.strip().lower()

# =====================================================
# Exercise 6 - title()
# =====================================================
print("Exercise 6")
# Task:
# Format a name.

reader_name = "anthony hennegan"

formatted_name = reader_name.title()

print(formatted_name)

# Questions:
#
# 1. What did the program print?
#   "Anthony Hennegan"
#  
# 2. What does title() do?
#   Capitalize the first letter of each word.
#
# 3. When might this be useful in the Library project?
#   When writing a name or a header.

# =====================================================
# Exercise 7 - Normalize User Input
# =====================================================
print("Exercise 7")
# Task:
# Ask the user a question and clean the answer before comparing it.

view_selection = input("Would you like to view our book selection? ")

view_selection = view_selection.strip().lower()

if view_selection == "yes":
    print("Ok, here is what we have.")
elif view_selection == "no":
    print("No worries. Have a nice day!")
else:
    print("Please type yes or no.")

# Try typing:
# yes
# Yes
# YES
#  yes
# yes 

# Questions:
#
# 1. Which versions of yes worked?
#   All of them.
#
# 2. Why did they work?
#   .strip() and .lower() standardized the responses
#
# 3. What would happen if you removed strip()?
#   The response with the space at the beginning and end would not work
#
# 4. What would happen if you removed lower()?
#   The response with uppercase strings would not work.


# =====================================================
# Reflection
# =====================================================

# Key Takeaways:
#
# - String methods transform text.
# - lower() converts text to lowercase.
# - upper() converts text to uppercase.
# - strip() removes whitespace from the beginning and end.
# - title() capitalizes the first letter of each word.
# - String methods return new strings.
# - To keep the transformed value, store the result in a variable.
# - Method chaining lets you apply multiple methods in one statement.
# - Normalizing input makes user responses easier to compare.


# Questions I still have:
#
#
#