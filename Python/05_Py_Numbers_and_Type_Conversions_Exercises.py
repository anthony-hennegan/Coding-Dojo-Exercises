"""
=====================================================
Lesson 007 - Numbers and Type Conversion
Exercise 001 - int(), float(), and str()
=====================================================

Objective:
Learn how to convert values between strings, integers, and floats.

Instructions:
- Read each section.
- Predict what will happen BEFORE running the code.
- Run the code in the terminal.
- Answer the questions in your own words.
"""


# =====================================================
# Exercise 1 - input() Returns a String
# =====================================================
print("Exercise 1")
# Task:
# Ask the user for a number and check its data type.

book_count = input("How many books do you own? ")

print(book_count)
print(type(book_count))

# Questions:
#
# 1. If you typed 20, what did Python print?
#   "20"
#   <class 'str'>
#
# 2. What data type was book_count?
#   A string.
#
# 3. Why is book_count not an integer yet?
#   Input always returns a string.


# =====================================================
# Exercise 2 - Convert String to Integer
# =====================================================
print("Exercise 2")
# Task:
# Convert the user's input into an integer.

book_count = input("How many books do you own? ")

book_count = int(book_count)

print(book_count)
print(type(book_count))

# Questions:
#
# 1. What did int() do?
#   Converted book_count to an integer.
#
# 2. What data type was book_count after conversion?
#   Integer.
#
# 3. Why is this useful?
#   Now we can do number comparison operations.


# =====================================================
# Exercise 3 - Numeric Comparison
# =====================================================
print("Exercise 3")
# Task:
# Convert input before comparing it to a number.

requested_books = input("How many books would you like to check out? ")
requested_books = int(requested_books)

if requested_books > 3:
    print("You can only check out 3 books at a time.")
else:
    print("Checkout amount approved.")

# Questions:
#
# 1. What happens if you type 2?
#   The program will run the else block.
#
# 2. What happens if you type 5?
#   The program will run the if block.
#
# 3. Why does this comparison work now?
#   Because the input response has been converted to an integer.

# =====================================================
# Exercise 4 - Convert String to Float
# =====================================================
print("Exercise 4")
# Task:
# Convert user input into a decimal number.

late_fee = input("What is the late fee amount? ")

late_fee = float(late_fee)

print(late_fee)
print(type(late_fee))

# Questions:
#
# 1. If you typed 1.50, what did Python print?
#   1.5
#   float
#
# 2. What data type was late_fee after conversion?
#   float
# 3. When would float() be more useful than int()?
#   When you need a decimal.

# =====================================================
# Exercise 5 - Convert Number to String
# =====================================================
print("Exercise 5")
# Task:
# Convert a number into a string.

book_count = 20

book_count_text = str(book_count)

print(book_count_text)
print(type(book_count_text))

# Questions:
#
# 1. What did str() do?
#   Converted book_count to a string.
#
# 2. What data type was book_count_text?
#   book_count_text was a string.
#
# 3. When might converting a number to a string be useful?
#   When the format requires a string.

# =====================================================
# Exercise 6 - Conversion Error
# =====================================================
print("Exercise 6")
# Task:
# Observe what happens when int() cannot convert the input.

book_count = input("Type a whole number: ")

book_count = int(book_count)

print(book_count)

# Try typing:
# 5
# five
# 5.5

# Questions:
#
# 1. What happened when you typed 5?
#   Python converted it to the integer 5 and printed it.
#
# 2. What happened when you typed five?
#   Value Error
#
# 3. What happened when you typed 5.5?
#   Value Error
#
# 4. Why did the invalid inputs fail?
#   int() can only convert values that represent whole numbers. 
#   "five" is word text and "5.5" represents a decimal, not a whole number.


# =====================================================
# Reflection
# =====================================================

# Key Takeaways:
#
# - input() always returns a string.
# - int() converts a value to an integer.
# - float() converts a value to a decimal number.
# - str() converts a value to a string.
# - Numeric input must be converted before doing math or numeric comparisons.
# - int() only works when the value can be converted into a whole number.
# - Invalid conversions cause errors.


# Questions I still have:
#
#
#