# Lesson 017 Exercises - Error Handling

# Exercise 1 - Age Conversion

* Ask the user for their age.
* Convert the response to an integer inside a `try` block.
* If the conversion succeeds, print the user's age.
* Catch `ValueError` if the conversion fails.
* Print:

```text
Please enter your age as a whole number.
```

* Test with:
  * `34`
  * `thirty-four`

---

# Exercise 2 - Item Quantity

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

* Test with:
  * `5`
  * `0`
  * `-3`
  * `five`

---

# Exercise 3 - Temperature Conversion

* Ask the user for a temperature in Fahrenheit.
* Convert the response to a float inside a `try` block.
* Convert Fahrenheit to Celsius using:

```python
celsius = (fahrenheit - 32) * 5 / 9
```

* Print the Celsius result.
* Display the result with two decimal places.
* Catch `ValueError` if the user enters invalid text.
* Print:

```text
Please enter a valid number.
```

---

# Exercise 4 - Simple Division

* Ask the user for two whole numbers.
* Convert both responses to integers inside a `try` block.
* Divide the first number by the second number.
* Catch `ValueError` if either response cannot be converted.
* Catch `ZeroDivisionError` if the second number is zero.
* Use separate `except` blocks.
* Print:

```text
Please enter whole numbers only.
```

* For division by zero, print:

```text
The second number cannot be zero.
```

---

# Exercise 5 - Product Selection

Start with:

```python
products = [
    "Hammer",
    "Saw",
    "Drill",
]
```

* Print each product with its list index.
* Ask the user to select a product number.
* Convert the response to an integer.
* Use the integer to access the selected product.
* Catch `ValueError` if the user enters text.
* Catch `IndexError` if the number does not exist in the list.
* Print:

```text
Please enter a whole number.
```

* For an invalid index, print:

```text
That product number does not exist.
```

* Test with:
  * `1`
  * `five`
  * `5`