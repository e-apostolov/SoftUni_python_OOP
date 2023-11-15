from typing import List, Optional


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __repr__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def find_book(self, title: str) -> Optional[Book]:
        book = next((b for b in self.books if b.title.lower() == title), None)
        return book


book = Book("Title1", "Testy Tester")
book2 = Book("Title", "Test Test")

library = Library()
print(library.books)
library.add_book(book)
print(library.find_book("Asd"))
print(library.find_book("title1"))


