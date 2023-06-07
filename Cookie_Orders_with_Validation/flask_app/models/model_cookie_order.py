from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db = "cookie_orders_schema"

class Cookie_order:
    def __init__( self, data ):
        self.id = data['id']
        self.customer_name = data['customer_name']
        self.cookie_type = data['cookie_type']
        self.number_of_boxes = data['number_of_boxes']

    @staticmethod
    def validate_order(cookie_order):
        valid = True
        if len(cookie_order['customer_name']) < 2:
            flash("Customer Name must be greater than 2 characters")
            valid = False
        if len(cookie_order['cookie_type']) < 2:
            flash("Cookie Type must be greater than 2 characters")
            valid = False
        if int(cookie_order['number_of_boxes']) < 1:
            flash("Number Of Boxes must be 1 or more")
            valid = False
        return valid

    @classmethod
    def get_all(cls):
        query = """SELECT * FROM cookie_orders"""
        results = connectToMySQL(db).query_db(query)
        return results

    @classmethod
    def save(cls, data):
        query = """INSERT INTO cookie_orders (customer_name, cookie_type, number_of_boxes)
                    VALUES(%(customer_name)s, %(cookie_type)s, %(number_of_boxes)s)"""
        result = connectToMySQL(db).query_db(query, data)
        return result

    @classmethod
    def get_order(cls, data):
        query = """SELECT * from cookie_orders WHERE id = %(id)s"""
        result = connectToMySQL(db).query_db(query, data)
        return result[0]

    @classmethod
    def change_order(cls, form_data, order_id):
        query = f"UPDATE cookie_orders SET customer_name = %(customer_name)s, cookie_type = %(cookie_type)s, number_of_boxes = %(number_of_boxes)s WHERE id = {order_id}"
        return connectToMySQL(db).query_db(query, form_data)
   

