# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the user table from our database
class User:
    DB = "users"
    def __init__( self,data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']

    # Now we use class methods to query our database

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.DB).query_db(query)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            users.append( user )
        return users

    # class method to add a new user to the database
    @classmethod
    def get_one(cls, user_id):
        query  = "SELECT * FROM userss WHERE id = %(id)s";
        data = {'id':user_id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])

    # create a new record in the database
    @classmethod
    def save(cls, data):
        query = """INSERT INTO users (first_name, last_name, email)
                    VALUES (%(first_name)s, %(last_name)s, %(email)s )"""
        #data is a dictionary that will be passed in from server.py
        result = connectToMySQL(cls.DB).query_db(query, data)
        print(result)
        return result
