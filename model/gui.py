import tkinter as tk
from tkinter import messagebox
from poe_code import Library

class LibraryGUI:
    def __init__(self, library):
        self.library = library

        self.window = tk.Tk()
        self.window.title("Library Management System")

        self.label_title = tk.Label(self.window, text="Library Management System", font=("Arial", 16))
        self.label_title.pack(pady=10)

        self.label_name = tk.Label(self.window, text="Library Name:")
        self.label_name.pack()
        self.entry_name = tk.Entry(self.window)
        self.entry_name.pack()

        self.label_location = tk.Label(self.window, text="Location:")
        self.label_location.pack()
        self.entry_location = tk.Entry(self.window)
        self.entry_location.pack()

        self.button_create = tk.Button(self.window, text="Create Library", command=self.create_library)
        self.button_create.pack(pady=10)

        self.button_display = tk.Button(self.window, text="Display Books", command=self.display_books)
        self.button_display.pack(pady=10)

        self.label_book = tk.Label(self.window, text="Book:")
        self.label_book.pack()
        self.entry_book = tk.Entry(self.window)
        self.entry_book.pack()

        self.button_add = tk.Button(self.window, text="Add Book", command=self.add_book)
        self.button_add.pack(pady=10)

        self.button_borrow = tk.Button(self.window, text="Borrow Book", command=self.borrow_book)
        self.button_borrow.pack(pady=10)

        self.button_return = tk.Button(self.window, text="Return Book", command=self.return_book)
        self.button_return.pack(pady=10)

    def create_library(self):
        name = self.entry_name.get()
        location = self.entry_location.get()
        self.library.name = name
        self.library.location = location
        messagebox.showinfo("Success", "Library created successfully!")

    def display_books(self):
        books = self.library.books
        if books:
            message = "\n".join(books)
        else:
            message = "No books in the library."
        messagebox.showinfo("Books in the Library", message)

    def add_book(self):
        book = self.entry_book.get()
        self.library.add_book(book)
        messagebox.showinfo("Success", f"Book '{book}' added to the library.")

    def borrow_book(self):
        book = self.entry_book.get()
        if self.library.borrow_book(book):
            messagebox.showinfo("Success", f"Book '{book}' borrowed successfully.")
        else:
            messagebox.showinfo("Error", f"Book '{book}' is not available in the library.")

    def return_book(self):
        book = self.entry_book.get()
        self.library.return_book(book)
        messagebox.showinfo("Success", f"Book '{book}' returned to the library.")

    def run(self):
        self.window.mainloop()

newLib = Library("School Library", "Khartoum")
# Create the GUI interface
gui = LibraryGUI(newLib)

# Run the GUI
gui.run()