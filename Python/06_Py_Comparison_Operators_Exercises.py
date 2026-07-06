"""
=====================================================
Lesson 008 - Comparison Operators
Exercise 001 - Comparing Values
=====================================================

Objective:
Learn how Python compares values using comparison operators.

Instructions:
- Read each section.
- Predict what will happen BEFORE running the code.
- Run the code in the terminal.
- Answer the questions in your own words.
"""


# =====================================================
# Exercise 1 - Equal To
# =====================================================

print("Exercise 1")

book_limit = 3

print(book_limit == 3)
print(book_limit == 5)

# Questions:
#
# 1. What did book_limit == 3 print?
#    True
#
# 2. What did book_limit == 5 print?
#    False
#
# 3. What does == check?
#    It checks whether one value is equal to another.

# =====================================================
# Exercise 2 - Not Equal To
# =====================================================

print("Exercise 2")

reader_name = "Anthony"

print(reader_name != "Bob")
print(reader_name != "Anthony")

# Questions:
#
# 1. What did reader_name != "Bob" print?
#    True
#
# 2. What did reader_name != "Anthony" print?
#    False
#
# 3. What does != check?
#    It checks whether a value is not equal to another.

# =====================================================
# Exercise 3 - Greater Than
# =====================================================

print("Exercise 3")

requested_books = 5
checkout_limit = 3

print(requested_books > checkout_limit)

# Questions:
#
# 1. What did the comparison print?
#    True
#
# 2. Why was the result True or False?
#    The result was true because the requested_books are greater than the checkout_limit.
#
# 3. When would > be useful in the Library project?
#    When there is need to know if a value is greater than a set limit.

# =====================================================
# Exercise 4 - Less Than
# =====================================================

print("Exercise 4")

requested_books = 2
checkout_limit = 3

print(requested_books < checkout_limit)

# Questions:
#
# 1. What did the comparison print?
#    True
#
# 2. Why was the result True or False?
#    It was true because requested_books is less than checkout_limit.
#
# 3. When would < be useful?
#    When there is need to know if a value is less than a set limit.

# =====================================================
# Exercise 5 - Greater Than or Equal To
# =====================================================

print("Exercise 5")

requested_books = 3
checkout_limit = 3

print(requested_books >= checkout_limit)

# Questions:
#
# 1. What did the comparison print?
#    True
#
# 2. Why is 3 >= 3 True?
#    Because the operator is greater than or equal to and 3 is equal to 3.
#
# 3. How is >= different from >?
#    > does not consider equal values as true.

# =====================================================
# Exercise 6 - Less Than or Equal To
# =====================================================

print("Exercise 6")

requested_books = 3
checkout_limit = 3

print(requested_books <= checkout_limit)

# Questions:
#
# 1. What did the comparison print?
#    True
#
# 2. Why is 3 <= 3 True?
#    The comparison operator accepts equal values as true.
#
# 3. How is <= different from <?
#    <= accepts equal values as true, but < does not.

# =====================================================
# Exercise 7 - Comparison in a Conditional
# =====================================================

print("Exercise 7")

requested_books = input("How many books would you like to check out? ")
requested_books = int(requested_books)

checkout_limit = 3

if requested_books <= checkout_limit:
    print("Checkout amount approved.")
else:
    print("You can only check out 3 books at a time.")

# Try typing:
# 1
# 3
# 4

# Questions:
#
# 1. What happened when you typed 1?
#    Checkout amount was approved.
#
# 2. What happened when you typed 3?
#    Checkout ammount was approved.
#
# 3. What happened when you typed 4?
#    Was told to check out limit is 3.
#
# 4. Why is <= useful here?
#    It lets us match the set checkout limit.

# =====================================================
# Exercise 8 - Assignment vs Comparison
# =====================================================

print("Exercise 8")

book_limit = 3

print(book_limit == 3)

# Questions:
#
# 1. What does book_limit = 3 do?
#    Assigns the value 3 to book_limit variable.
#
# 2. What does book_limit == 3 do?
#    Checks if book_limit value is equal to 3.
#
# 3. Why are = and == not the same?
#    = assigns value, and == compares values.

# =====================================================
# Reflection
# =====================================================

# Key Takeaways:
#
# - = assigns a value.
# - == checks whether two values are equal.
# - != checks whether two values are not equal.
# - > checks whether the left value is greater than the right value.
# - < checks whether the left value is less than the right value.
# - >= checks whether the left value is greater than or equal to the right value.
# - <= checks whether the left value is less than or equal to the right value.
# - Comparisons return True or False.
# - Comparisons are commonly used inside conditionals.


# Questions I still have:
#
#
#