class Library():
    def __init__(self, name):
        self.name = name
        self.books = []
        
    def display_books(self):
        for book in self.books:
            print(book)
    
    def add_book(self, book):
        self.books.append(book)
        self.books.append()
        

library_name = "Tracy Library"

library = Library(library_name)

library.add_book("book1")
library.display_books()

