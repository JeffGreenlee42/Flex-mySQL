from flask_app.config.mysqlconnection import connectToMySQL

db = "dojos_and_ninjas_schema"

class Dojo:
    def __init__( self,data ):
        self.id = data["id"]
        self.name = data["name"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(db).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(dojo)
        return dojos

    @classmethod
    def save(cls, data):
        query = """INSERT INTO dojos (name)
                    VALUES (%(name)s )"""
        results = connectToMySQL(db).query_db(query, data)
        return results
    
    @classmethod
    def get_one(cls, dojo_id):
        dojo_id = dojo_id
        dojo_name = get_dojo_name(dojo_id)
        print (f"dojo_id is: {dojo_id}")
        # print (f"dojo_name is: {dojo_name}")
        query = f"SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = {dojo_id};"
        results = connectToMySQL(db).query_db(query)
        print(results)
        ninjas = []
        for ninja in results:
            ninja_data = {
                # 'dojo_name' : dojo_name,
                'id' : ninja['ninjas.id'],
                'first_name' : ninja['first_name'],
                'last_name' : ninja['last_name'],
                'age' : ninja['age'],
                'created_at' : ninja['ninjas.created_at'],
                'updated_at' : ninja['ninjas.updated_at']
            }
            ninjas.append(ninja_data)
        return ninjas

    @classmethod
    def get_dojo_name(cls, dojo_id):
        dojo_id = int(dojo_id)
        data = {
            "id": dojo_id
        }
        print(f"model_dojos dojo_id is: {dojo_id}")
        query = f"SELECT name FROM dojos WHERE id = {dojo_id}"
        print(f"get_dojo_name query is: {query}")
        dojo_name = connectToMySQL(db).query_db(query, data)
        return dojo_name

