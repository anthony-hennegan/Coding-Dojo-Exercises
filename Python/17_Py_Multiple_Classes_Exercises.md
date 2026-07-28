# Lesson 032 — Multiple Classes Guided Exercise

## Requirements

Create a `Book` class.

Each `Book` object must have:

- `title`
- `author`
- `checked_out`, starting as `False`

Add these methods:

- `checkout()`
  - Return `False` if already checked out.
  - Otherwise set `checked_out` to `True` and return `True`.

- `return_book()`
  - Return `False` if already available.
  - Otherwise set `checked_out` to `False` and return `True`.

Create a `Library` class.

Each `Library` object must have:

- `name`
- an empty `books` list

Add these methods:

- `add_book(book)`
  - Add the supplied `Book` object to the library's collection.

- `find_book(title)`
  - Search case-insensitively.
  - Return the matching `Book` object.
  - Return `None` if no book matches.

Create:

- One `Library` object
- At least three different `Book` objects

Add the books to the library.

Use `find_book()` to locate one book.

Call that book's `checkout()` method.

Print enough information to confirm:

- The book was found.
- Its checkout status changed.
- The object returned by `find_book()` is the same object stored in the library.