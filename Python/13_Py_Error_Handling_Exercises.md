# Lesson 017 Exercises - Error Handling

Complete each exercise as a separate Python file.

Run each file from the terminal and test every required input.

---

# Exercise 1 - Age Conversion

Create:

```text
exercise_1_age.py
```

## Requirements

* Ask the user for their age.
* Convert the response to an integer inside a `try` block.
* If the conversion succeeds, print the user's age.
* Catch `ValueError` if the conversion fails.

Example valid output:

```text
Enter your age: 34
You are 34 years old.
```

Invalid input message:

```text
Please enter your age as a whole number.
```

## Test With

```text
34
thirty-four
```

---

# Exercise 2 - Item Quantity

Create:

```text
exercise_2_quantity.py
```

## Requirements

* Ask how many items the user wants to purchase.
* Convert the response to an integer inside a `try` block.
* If the number is greater than `0`, print the requested quantity.
* If the number is `0` or less, print:

```text
Quantity must be greater than zero.
```

* Catch `ValueError` if the conversion fails.
* Print:

```text
Please enter a valid whole number.
```

## Test With

```text
5
0
-3
five
```

---

# Exercise 3 - Temperature Conversion

Create:

```text
exercise_3_temperature.py
```

## Requirements

* Ask the user for a temperature in Fahrenheit.
* Convert the response to a float inside a `try` block.
* Convert Fahrenheit to Celsius using:

```python
celsius = (fahrenheit - 32) * 5 / 9
```

* Print the Celsius result.
* Display the result with two decimal places.
* Catch `ValueError` if the user enters invalid text.

Example valid output:

```text
Enter a temperature in Fahrenheit: 75
75.0 degrees Fahrenheit is 23.89 degrees Celsius.
```

Invalid input message:

```text
Please enter a valid number.
```

---

# Exercise 4 - Simple Division

Create:

```text
exercise_4_division.py
```

## Requirements

* Ask the user for two whole numbers.
* Convert both responses to integers inside a `try` block.
* Divide the first number by the second number.
* Catch `ValueError` if either response cannot be converted.
* Catch `ZeroDivisionError` if the second number is zero.
* Use separate `except` blocks.

Example valid output:

```text
Enter the first number: 10
Enter the second number: 2
Result: 5.0
```

Invalid number message:

```text
Please enter whole numbers only.
```

Division-by-zero message:

```text
The second number cannot be zero.
```

---

# Exercise 5 - Product Selection

Create:

```text
exercise_5_product.py
```

Start with:

```python
products = [
    "Hammer",
    "Saw",
    "Drill",
]
```

## Requirements

* Print each product with its list index.

Example:

```text
0. Hammer
1. Saw
2. Drill
```

* Ask the user to select a product number.
* Convert the response to an integer.
* Use the integer to access the selected product.
* Catch `ValueError` if the user enters text.
* Catch `IndexError` if the number does not exist in the list.

Example valid output:

```text
You selected Saw.
```

Invalid number message:

```text
Please enter a whole number.
```

Invalid index message:

```text
That product number does not exist.
```

## Test With

```text
1
five
5
```