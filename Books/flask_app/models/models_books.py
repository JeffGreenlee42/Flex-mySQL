from flask_app.config.mysqlconnection import connectToMySQL

db = "books_schema"

class Book:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.num_of_pages = data["num_of_pages"]

    @classmethod
    def get_all(cls):
        query = """SELECT * FROM books"""
        results = connectToMySQL(db).query_db(query)
        all_books = []
        for book in results:
            all_books.append(book)
        return all_books

    @classmethod
    def save(cls, data):
        query = """INSERT INTO books (title, num_of_pages)
                    VALUES (%(title)s, %(num_of_pages)s)"""
        results = connectToMySQL(db).query_db(query, data)
        return results



