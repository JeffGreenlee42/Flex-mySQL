from flask_app import app
from flask import Flask, render_template, redirect, request, session
from flask_app.models.model_dojos import Dojo
from flask_app.models.model_ninjas import Ninja

@app.route("/")
def index():
    all_dojos = Dojo.get_all()
    return render_template("dojo.html", all_dojos = all_dojos)

@app.route("/add_new_dojo", methods=["POST"])
def add_new_dojo():
    result = Dojo.save(request.form)
    return redirect("/")

@app.route("/dojos/get_one/<int:dojo_id>")
def get_dojo_ninjas(dojo_id):
    name = Dojo.get_dojo_name(dojo_id)
    print(f"name is: {name}")
    dojo_name = name[0]['name']
    print("dojo_name is: {dojo_name}")
    dojo_ninjas = Ninja.get_dojo_ninjas(dojo_id)
    return render_template('dojo_show.html', dojo_ninjas = dojo_ninjas, dojo_name = dojo_name)

@app.route("/ninjas/new_ninja")
def new_ninja():
    all_dojos = Dojo.get_all()
    print(f"From new_ninja - all_dojos is: {all_dojos}")
    return render_template("new_ninja.html", all_dojos = all_dojos)