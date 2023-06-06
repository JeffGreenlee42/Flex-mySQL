# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

db = "users"

class User:

    def __init__( self,data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']

    @staticmethod
    def is_duplicate_email(email):
        # email = {
        #     "email": email
        # }
        is_duplicate = False
        query = f"SELECT * FROM users where email = '{email}'"
        result = connectToMySQL(db).query_db(query)
        result_count = len(result)
        if len(result) > 0:
            flash("Email already exists! please choose another!")
            is_duplicate = True
        return is_duplicate


    @staticmethod
    def validate_user(user):
        valid = True
        if len(user['first_name']) < 3:
            flash("Name must be greater than 3 characters")
            valid = False
        if len(user['last_name']) < 3:
            flash("Name must be greater than 3 characters")
            valid = False
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(user['email']):
            flash("invalid email address!")
            valid = False
        return valid

 
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(db).query_db(query)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            users.append( user )
        return users

    # class method to add a new user to the database
    @classmethod
    def get_one(cls, data):
        query  = """SELECT * FROM users WHERE id = %(id)s"""
        results = connectToMySQL(db).query_db(query, data)
        return (results[0])

 
    # create a new record in the database
    @classmethod
    def save(cls, data):
        query = """INSERT INTO users (first_name, last_name, email)
                    VALUES (%(first_name)s, %(last_name)s, %(email)s )"""
        result = connectToMySQL(db).query_db(query, data)
        return result

    @classmethod
    def update(cls, form_data, user_id):
        query = f"UPDATE users SET first_name = %(first_name)s,last_name = %(last_name)s, email = %(email)s WHERE id = {user_id}"
        return connectToMySQL(db).query_db(query, form_data)

    @classmethod
    def delete(cls, form_data, user_id):
        query = f"DELETE FROM users WHERE id = {user_id}"
        return connectToMySQL(db).query_db(query, form_data)