from flask_app.config.mysqlconnection import connectToMySQL

db = "dojos_and_ninjas_schema"

class Dojos:

    def __init__( self,data ):
        self.id = data["id"]
        self.name = data["name"]

    @classmethod
    def get_all():
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(db).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(dojo)
        return dojos

    @classmethod
    def save(data):
        query = """INSERT INTO dojos (name)
                    VALUES (%(name)s )"""
        results = connectToMySQL(db).query_db(query, data)
        return results
    
    @classmethod
    def get_one(dojo_id):
        query = """
                SELECT * FROM dojos
                JOIN ninjas
                ON dojos.id = ninjas.dojo_id;
                """