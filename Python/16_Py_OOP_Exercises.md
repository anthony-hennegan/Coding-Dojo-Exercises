# Lesson 026 — Exercises
## Classes, Objects, `self`, and References

---

# Rules

For every exercise:

1. Do NOT run the code immediately.
2. Predict exactly what will happen.
3. Write your prediction.
4. Then run the code.
5. If you were incorrect, explain:
   - Result.
   - This happened because...
   - Rule.

---

# Exercise 1 — Class or Object?

For each statement, identify whether it describes a **Class** or an **Object**.

1.

```
Acts as a blueprint.
```

Answer:

---

2.

```
Stores its own data.
```

Answer:

---

3.

```
Can create many independent instances.
```

Answer:

---

4.

```
Represents one individual thing.
```

Answer:

---

# Exercise 2 — Constructor Timing

Without running the code:

```python
class Book:

    def __init__(self):
        print("Creating book")


book1 = Book()

book2 = Book()

book3 = Book()
```

Questions:

1. What prints?

2. How many Book objects are created?

3. How many Book classes exist?

---

# Exercise 3 — What Is self?

Without running the code:

```python
class Book:

    def __init__(self, title):
        self.title = title


book = Book("Dune")
```

Questions:

1. What does `self` refer to?

2. Does `self` create the object?

3. When does `__init__()` run?

---

# Exercise 4 — References

Without running the code:

```python
book1 = Book("Dune")

book2 = book1
```

Questions:

1. How many Book objects exist?

2. How many variables exist?

3. Which variables reference the object?

---

# Exercise 5 — Updating Through References

Without running the code:

```python
book1 = Book("Dune")

book2 = book1

book1.title = "Foundation"

print(book2.title)
```

Questions:

1. What prints?

2. Why?

---

# Exercise 6 — Lists Store References

Without running the code:

```python
books = []

book = Book("Dune")

books.append(book)

book.title = "Foundation"

print(books[0].title)
```

Questions:

1. What prints?

2. Why?

---

# Exercise 7 — Instance Method

Without running the code:

```python
class Book:

    def __init__(self):
        self.checked_out = False

    def checkout(self):
        self.checked_out = True


book = Book()

book.checkout()
```

Questions:

1. Which object does `self` refer to?

2. What is the final value of `checked_out`?

---

# Exercise 8 — Return Values

Without running the code:

```python
class Book:

    def checkout(self):

        if self.checked_out:
            return False

        self.checked_out = True
        return True
```

Questions:

1. What does the method return if the book is available?

2. What does it return if the book is already checked out?

3. Why are those return values useful?

---

# Exercise 9 — Reading Code

Read the code.

```python
if book.checkout():
    save_books(books)
```

Explain the execution order.

Write every major step.

---

# Exercise 10 — Responsibility

For each responsibility, write which part of the application should own it.

Choices:

- Book
- Library
- Storage
- Main
- Menu/UI

Responsibilities:

1. Check whether a book is already checked out.

2. Save data to JSON.

3. Display success messages.

4. Search for a book by title.

5. Coordinate the program.

---

# Exercise 11 — Explain self

Pretend you're teaching another student.

In your own words explain:

- What is `self`?
- Why does Python need it?
- Why can't Python simply use the caller's variable name?

Do not use the phrase:

> "Because Python says so."

Explain the reasoning.

---

# Exercise 12 — The Big Mental Model

Without writing code, explain the complete process that happens when Python executes:

```python
book = Book("Dune")
```

Include:

- object creation
- `__init__`
- `self`
- references
- assignment to `book`

Your explanation should be detailed enough that someone who has never seen classes before could follow the entire process.