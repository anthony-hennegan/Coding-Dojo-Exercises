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

search_title = input("Enter a book title: ").strip().lower()
print("")

found_book = False

for book in books:
    if book["title"].lower() == search_title:
        found_book = True
        
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print("")
        
        if not book['checked_out']:
            print("Is available for check out.")
        else:
            print("Not available for checkout.")
        break

if not found_book:
    print("Book not found.")
    