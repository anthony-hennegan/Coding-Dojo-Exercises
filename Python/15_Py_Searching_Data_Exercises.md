# Lesson 019 - Guided Exercise: Searching Data

## Exercise

Start with:

```python
books = [
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "checked_out": False
    },
    {
        "title": "Dune",
        "author": "Frank Herbert",
        "checked_out": True
    },
    {
        "title": "Foundation",
        "author": "Isaac Asimov",
        "checked_out": False
    }
]
```

## Requirements

- Ask the user for a book title.
- Clean the input using the techniques you've already learned.
- Search the list of dictionaries for a matching title.
- If the book is found:
  - Print the title.
  - Print the author.
  - Print whether the book is available or checked out.
- Stop searching after finding the first match.
- If no matching book is found, print:

```text
Book not found.
```

### Bonus

After you get the basic search working, make the search **case-insensitive** so all of these work:

```text
dune
Dune
DUNE
```

without changing the stored book titles.