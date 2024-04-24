from book import Book
from member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully.")

    def add_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' added successfully.")

    def search_books(self, title=None, author=None):
        results = []
        for book in self.books:
            if title and title.lower() in book.title.lower():
                results.append(book)
            elif author and author.lower() in book.author.lower():
                results.append(book)
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def borrow_book(self, member, book):
        if book in self.books and member in self.members:
            member.borrow_book(book)
        else:
            print("Invalid book or member.")

    def return_book(self, member, book):
        if book in self.books and member in self.members:
            member.return_book(book)
        else:
            print("Invalid book or member.")


    def manage_member_info(self, member_id=None, action=None, new_member=None):
        # Actions: 'add' to add a new member, 'update' to update member information
        if action == 'add' and new_member:
            self.add_member(new_member)
        elif action == 'update' and member_id:
            member = next((m for m in self.members if m.member_id == member_id), None)
            if member:
                print(f"Current Info: {member.get_info()}")
                # Update member info here
                # For example, update the name of the member
                new_name = input("Enter new name for the member: ")
                if new_name:
                    member.name = new_name
                    print("Member info updated.")
            else:
                print("Member not found.")
