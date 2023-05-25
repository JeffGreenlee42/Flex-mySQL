from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import models_authors


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

    @classmethod
    def get_book(cls, data):
        # print(f"get_book data is {data}")
        query = """SELECT * FROM books
                    WHERE id = %(id)s
                """
        results = connectToMySQL(db).query_db(query, data)
        # print(f"From get_author - results = {results}")
        return results

    @classmethod
    def get_authors_selected_book(cls, book_id):
        print(f"from get_authors_slected_book: book_id is {book_id}")
        query = """SELECT * FROM favorites
                    JOIN authors ON favorites.author_id = authors.id
                    WHERE book_id = %(id)s"""
        results = connectToMySQL(db).query_db(query, book_id)
        return results
