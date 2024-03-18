from database import Database


class BookManager:
    def __init__(self, db_name):
        self.db = Database(db_name)

    def add_book(self, title, author, description, genre):
        self.db.add_book(title, author, description, genre)

    def delete_book(self, book_id):
        self.db.delete_book(book_id)

    def get_books_by_genre(self, genre):
        return self.db.get_books_by_genre(genre)

    def search_books(self, keyword):
        return self.db.search_books(keyword)

    def get_all_books(self):
        return self.db.get_all_books()

    def close_connection(self):
        self.db.close_connection()
