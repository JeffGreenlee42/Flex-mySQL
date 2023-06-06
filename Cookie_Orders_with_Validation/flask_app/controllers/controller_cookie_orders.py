from flask_app import app
from flask import Flask, render_template, redirect, request, session
from flask_app.models.model_cookie_order import Cookie_order

@app.route("/cookie_orders")
def index():
    cookie_orders = Cookie_order.get_all()
    return render_template("index.html", cookie_orders = cookie_orders)

@app.route("/cookie_orders/new_order")
def new_order():
    return render_template("new_order.html")

@app.route("/cookie_orders/create", methods=["POST"])
def create():
    customer_name = request.form['customer_name']
    cookie_type = request.form['cookie_type']
    number_of_boxes = request.form['number_of_boxes']
    if not Cookie_order.validate_order(request.form):
        return render_template("new_order.html", customer_name = customer_name, cookie_type = cookie_type, number_of_boxes = number_of_boxes)
    user_id = Cookie_order.save(request.form)
    return redirect("/cookie_orders")
    
app.route("/cookie_orders/get_order/<int:order_id>")
def get_order(order_id):
    data = {
        "id": order_id
    }
    order = Cookie_order.get_order(data)
    print("next line is rendering change_order.html")
    return render_template("change_order.html", data)