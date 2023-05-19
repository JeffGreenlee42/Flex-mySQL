from flask_app import app
from flask import Flask, render_template, redirect, request, session
from flask_app.models.model_dojos import Dojos

@app.route("/")
def index():
    dojos = Dojos.get_all()
    return render_template("dojo.html", all_dojos = dojos)

@app.route("/add_new_dojo", methods=["POST"])
def add_new_dojo():
    result = Dojos.save(request.form)
    return redirect("/")

@app.route("/dojos/get_one/<int:dojo_id>")
def get_one(dojo_id):
    
