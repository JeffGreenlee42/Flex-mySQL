from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import models_books

db = "books_schema"

class Author:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]

    @classmethod
    def get_all(cls):
        query = """SELECT * FROM authors"""
        results = connectToMySQL(db).query_db(query)
        all_authors = []
        for author in results:
            all_authors.append(author)
        # print(f"From Authors - get_all: {all_authors}")
        return all_authors

    @classmethod
    def save(cls, data):
        query = """INSERT INTO authors (name)
                    VALUES (%(name)s)"""
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def get_author(cls, data):
        print(f"get_author data is {data}")
        query = """SELECT * FROM authors
                    WHERE id = %(id)s
                """
        results = connectToMySQL(db).query_db(query, data)
        print(f"From get_author - results = {results}")
        return results

    @classmethod
    def create_author_favorite(cls, data):
        query = """INSERT INTO favorites (author_id, book_id)
                    VALUES (%(author_id)s, %(book_id)s)"""
        result = connectToMySQL(db).query_db(query, data)
        return result
    
    @classmethod
    def get_author_favorites(cls, author_id):
        print(f"from get_autghor_favorites: author_id is = {author_id}")
        query = """SELECT * from favorites
                    JOIN books ON favorites.book_id = books.id
                    WHERE author_id = %(id)s"""
        print(f"query is: {query}")
        results = connectToMySQL(db).query_db(query, author_id)
        return results