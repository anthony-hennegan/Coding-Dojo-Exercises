# Lesson 018 Exercises - while Loops and Input Validation

# Exercise 1 - Password Validation

## Requirements

* Ask the user to enter a password.
* Keep asking until the password is exactly:

```text
python123
```

* If the password is incorrect, print:

```text
Incorrect password.
```

* When the correct password is entered, print:

```text
Access granted.
```

---

# Exercise 2 - Positive Number

## Requirements

* Ask the user to enter a whole number.
* Continue asking until they enter a valid integer greater than zero.
* Use `try` and `except ValueError`.
* If the conversion fails, print:

```text
Please enter a whole number.
```

* If the number is less than or equal to zero, print:

```text
Number must be greater than zero.
```

* When a valid number is entered, print:

```text
Accepted.
```

---

# Exercise 3 - Menu Selection

Start with:

```python
menu = [
    "View Books",
    "Check Out Book",
    "Exit"
]
```

## Requirements

* Display the menu with its index numbers.
* Ask the user to choose a menu option.
* Continue asking until the user enters a valid menu number.
* Use `try` and `except ValueError`.
* If the number is outside the list, print:

```text
That menu option does not exist.
```

* When a valid option is entered, print:

```text
You selected: <menu option>
```

---

# Exercise 4 - Shopping Quantity

## Requirements

* Ask the user how many items they want to buy.
* Continue asking until:
  * the input converts to an integer
  * the number is greater than zero
  * the number is less than or equal to 20
* Use `try` and `except ValueError`.
* Print:

```text
Please enter a whole number.
```

for invalid input.

* Print:

```text
Quantity must be between 1 and 20.
```

for numbers outside the allowed range.

* When valid, print:

```text
Order accepted.
```

---

# Exercise 5 - Simple ATM

## Requirements

* Start with:

```python
balance = 150.00
```

* Ask the user how much money they want to withdraw.
* Continue asking until:
  * the input converts to a float
  * the withdrawal amount is greater than zero
  * the withdrawal amount is less than or equal to the balance
* Use `try` and `except ValueError`.
* Print:

```text
Please enter a valid amount.
```

for invalid input.

* Print:

```text
Insufficient funds.
```

when the withdrawal exceeds the balance.

* Print:

```text
Withdrawal amount must be greater than zero.
```

when appropriate.

* After a successful withdrawal:
  * subtract the withdrawal from the balance
  * print the remaining balance with two decimal places
  * exit the loop

---

## Reflection

Time to Complete:

Syntax I Forgot:

Concepts I Was Unsure About:

Mistakes I Made:

Questions I Have: