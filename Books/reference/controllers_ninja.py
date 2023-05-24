from flask_app import app
from flask import Flask, render_template, redirect, request, session
from flask_app.models.model_dojos import Dojos
from flask_app.models.model_ninjas import Ninja

@app.route("/")
def index():
    all_dojos = Dojos.get_all()
    return render_template("dojo.html", all_dojos = all_dojos)

@app.route("/add_new_dojo", methods=["POST"])
def add_new_dojo():
    result = Dojos.save(request.form)
    return redirect("/")

@app.route("/dojos/get_one/<int:dojo_id>")
def get_dojo_ninjas(dojo_id):
    dojo_ninjas = Ninja.get_dojo_ninjas(dojo_id)
    print(f"dojo_ninjas is: {dojo_ninjas}")
    return render_template('dojo_show.html', dojo_ninjas = dojo_ninjas)
