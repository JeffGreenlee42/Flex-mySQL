from flask_app.config.mysqlconnection import connectToMySQL

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
        return all_authors

    @classmethod
    def save(cls, data):
        query = """INSERT INTO authors (name)
                    VALUES (%(name)s)"""
        results = connectToMySQL(db).query_db(query, data)
        return results

