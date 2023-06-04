from flask_app import app
from flask import Flask, render_template, redirect, request, session
from flask_app.models.model_cookie_order import Cookie_orders

@app.route("/")
def index():
    # users = Cookie_orders.get_all()
    return render_template("index.html")
