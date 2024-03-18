from book_manager import BookManager


def display_menu():
    print("library Management System")
    print("[1] Add a new book")
    print("[2] Delete a book")
    print("[3] Search for a book")
    print("[4] Display all books")
    print("[5] Display books by genre")
    print("[6] Exit")


class UserInterface:
    def __init__(self, db_name):
        self.book_manager = BookManager(db_name)

    def add_book(self):
        title = input("enter the title of the book: ")
        author = input("enter the author of the book: ")
        description = input("enter the description of the book: ")
        genre = input("enter the genre of the book: ")
        self.book_manager.add_book(title, author, description, genre)
        print("book added successfully")

    def delete_book(self):
        book_id = int(input("enter the ID of the book you want to delete: "))
        self.book_manager.delete_book(book_id)
        print("book deleted successfully")

    def search_books(self):
        keyword = input("enter keyword to search for: ")
        search_results = self.book_manager.search_books(keyword)
        if search_results:
            print("search results:")
            for book in search_results:
                print(book)
        else:
            print("no books found matching the keyword.")

    def display_all_books(self):
        all_books = self.book_manager.get_all_books()
        print("all books:")
        for book in all_books:
            print(book)

    def display_books_by_genre(self):
        genre = input("enter the genre to display books: ")
        genre_books = self.book_manager.get_books_by_genre(genre)
        print(f"books in {genre} genre:")
        for book in genre_books:
            print(book)

    def run(self):
        while True:
            display_menu()
            choice = input("enter your choice: ")
            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.delete_book()
            elif choice == "3":
                self.search_books()
            elif choice == "4":
                self.display_all_books()
            elif choice == "5":
                self.display_books_by_genre()
            elif choice == "6":
                print("Exiting...")
                self.book_manager.close_connection()
                break
            else:
                print("invalid choice, please try again.")
