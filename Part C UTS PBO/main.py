from library import Library
from book import Book
from member import Member

def main():
    # Initialize library
    library = Library()

    # Add some initial books and members
    print('=== RENDER INITIAL OBJECTS ===')
    library.add_book(Book("Book A", "Author A", "ISBN001"))
    library.add_book(Book("Book B", "Author B", "ISBN002"))

    library.add_member(Member("Member A", "MEM001"))
    library.add_member(Member("Member B", "MEM002"))

    # Interactive menu
    while True:
        print("\n------------------------------")
        print("Welcome to UKRIDA Virtual Library")
        print("------------------------------")
        print("[1] Librarian")
        print("[2] Member")
        print("[0] Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Librarian options
            print("\nLibrarian options:")
            print("[1] Add new book")
            print("[2] Search for books")
            print("[3] Manage member information")
            print("[4] Go back")

            librarian_choice = input("Enter your choice: ")

            if librarian_choice == "1":
                # Add new book
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                isbn = input("Enter book ISBN: ")
                book = Book(title, author, isbn)
                library.add_book(book)

            elif librarian_choice == "2":
                # Search for books
                search_option = input("Search by (1) Title or (2) Author? ")
                if search_option == "1":
                    title = input("Enter book title: ")
                    library.search_books(title=title)
                elif search_option == "2":
                    author = input("Enter book author: ")
                    library.search_books(author=author)

            elif librarian_choice == "3":
                # Manage member information
                member_id = input("Enter member ID: ")
                action = input("Choose action (add/update): ")
                if action == "add":
                    name = input("Enter member name: ")
                    new_member = Member(name, member_id)
                    library.manage_member_info(member_id, action=action, new_member=new_member)
                elif action == "update":
                    library.manage_member_info(member_id, action=action)

        elif choice == "2":
            # Member options
            print("\nMember options:")
            print("1. Search for books")
            print("2. Borrow book")
            print("3. Return book")
            print("4. Go back")

            member_choice = input("Enter your choice: ")

            if member_choice == "1":
                # Search for books
                search_option = input("Search by (1) Title or (2) Author? ")
                if search_option == "1":
                    title = input("Enter book title: ")
                    library.search_books(title=title)
                elif search_option == "2":
                    author = input("Enter book author: ")
                    library.search_books(author=author)

            elif member_choice == "2":
                # Borrow book
                member_id = input("Enter your member ID: ")
                member = next((m for m in library.members if m.member_id == member_id), None)
                if member:
                    isbn = input("Enter book ISBN: ")
                    book = next((b for b in library.books if b.isbn == isbn), None)
                    if book:
                        library.borrow_book(member, book)
                    else:
                        print("Book not found.")
                else:
                    print("Member not found.")

            elif member_choice == "3":
                # Return book
                member_id = input("Enter your member ID: ")
                member = next((m for m in library.members if m.member_id == member_id), None)
                if member:
                    isbn = input("Enter book ISBN: ")
                    book = next((b for b in library.books if b.isbn == isbn), None)
                    if book:
                        library.return_book(member, book)
                    else:
                        print("Book not found.")
                else:
                    print("Member not found.")

        elif choice == "0":
            # Exit the program
            print("Thank you for using UKRIDA Virtual Library. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
