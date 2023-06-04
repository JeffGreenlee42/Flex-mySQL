from flask_app.config.mysqlconnection import connectToMySQL

db = "users"

class Cookie_orders:
    def __init__( self,data ):
        self.id = data['id']
        self.customer_name = data['customer_name']
        self.cookie_type = data['cookie_type']
        self.number_of_boxes = data['number_of_boxes']
