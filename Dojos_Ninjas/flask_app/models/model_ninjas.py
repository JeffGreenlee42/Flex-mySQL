from flask_app.config.mysqlconnection import connectToMySQL

db = "dojos_and_ninjas_schema"

class Ninja:
    def __init__( self,data ):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.dojo_id = data["dojo_id"]

    @classmethod
    def get_dojo_ninjas(cls, dojo_id):
        dojo_id = dojo_id
        print (f"Model_ninjas get_dojo_ninjas dojo_id is: {dojo_id}")
        query = f"SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = {dojo_id};"
        results = connectToMySQL(db).query_db(query)
        print(results)
        ninjas = []
        for ninja in results:
            ninja_data = {
                # 'dojo_name' : ['name'],
                'id' : ninja['idNinjas'],
                'first_name' : ninja['first_name'],
                'last_name' : ninja['last_name'],
                'age' : ninja['age'],
                'dojo_id' : ninja['dojo_id'],
                'created_at' : ninja['ninjas.created_at'],
                'updated_at' : ninja['ninjas.updated_at']
            }
            ninjas.append(ninja_data)
        return ninjas

    @classmethod
    def save(cls, data):
        print(f"data from model_ninjas save {data}")
        print("%(dojo_id)s")
        query = """INSERT INTO ninjas (first_name, last_name, age, dojo_id)
                VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)"""
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def get_ninja(cls, ninja_id):
        query = f"SELECT * FROM ninjas WHERE idNinjas = {ninja_id}"
        results =  connectToMySQL(db).query_db(query, ninja_id)

    @classmethod
    def update(cls, form_data, ninja_id):
        query = f"UPDATE ninjas SET dojo_id = %(dojo_id), first_name = %(first_name)s,last_name = %(last_name)s, age = %(age)s WHERE id = {ninja_id}"
        return connectToMySQL(db).query_db(query, form_data)