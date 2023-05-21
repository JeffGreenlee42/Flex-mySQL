from flask_app.config.mysqlconnection import connectToMySQL

db = "dojos_and_ninjas_schema"

class Ninja:
    def __init__( self,data ):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]

    @classmethod
    def get_dojo_ninjas(cls, dojo_id):
        dojo_id = dojo_id
        print (f"dojo_id is: {dojo_id}")
        query = f"SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojos_id WHERE dojos.id = {dojo_id};"
        results = connectToMySQL(db).query_db(query)
        print(results)
        ninjas = []
        for ninja in results:
            ninja_data = {
                'dojo_name' : ['name'],
                'id' : ninja['idNinjas'],
                'first_name' : ninja['first_name'],
                'last_name' : ninja['last_name'],
                'age' : ninja['age'],
                'created_at' : ninja['ninjas.created_at'],
                'updated_at' : ninja['ninjas.updated_at']
            }
            ninjas.append(ninja_data)
        return ninjas