class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            self.borrowed_books.append(book)
            book.set_available(False)
            print(f"Book '{book.title}' borrowed successfully.")
        else:
            print(f"Book '{book.title}' is currently unavailable.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.set_available(True)
            print(f"Book '{book.title}' returned successfully.")
        else:
            print(f"You have not borrowed the book '{book.title}'.")

    def get_info(self):
        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": [book.title for book in self.borrowed_books]
        }
