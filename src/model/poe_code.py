class Library:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.books = []

    def display_details(self):
        print(f"Library Name: {self.name}")
        print(f"Location: {self.location}")

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book}' added to the library.")

    def display_books(self):
        if self.books:
            print("Books in the Library:")
            for book in self.books:
                print(book)
        else:
            print("No books in the library.")

    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book}' borrowed successfully.")
        else:
            print(f"Book '{book}' is not available in the library.")

    def return_book(self, book):
        self.books.append(book)
        print(f"Book '{book}' returned to the library.")