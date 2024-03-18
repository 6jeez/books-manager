import sqlite3


class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS books (
                            id INTEGER PRIMARY KEY,
                            title TEXT,
                            author TEXT,
                            description TEXT,
                            genre TEXT)''')
        self.conn.commit()

    def add_book(self, title, author, description, genre):
        self.cur.execute('''INSERT INTO books (title, author, description, genre)
                            VALUES (?, ?, ?, ?)''', (title, author, description, genre))
        self.conn.commit()

    def delete_book(self, book_id):
        self.cur.execute('''DELETE FROM books WHERE id = ?''', (book_id,))
        self.conn.commit()

    def get_books_by_genre(self, genre):
        self.cur.execute('''SELECT * FROM books WHERE genre = ?''', (genre,))
        return self.cur.fetchall()

    def search_books(self, keyword):
        self.cur.execute('''SELECT * FROM books WHERE title LIKE ? OR author LIKE ?''',
                         ('%' + keyword + '%', '%' + keyword + '%'))
        return self.cur.fetchall()

    def get_all_books(self):
        self.cur.execute('''SELECT id, title, author FROM books''')
        return self.cur.fetchall()

    def close_connection(self):
        self.conn.close()
