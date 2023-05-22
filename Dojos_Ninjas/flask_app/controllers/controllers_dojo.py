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
    dojo_name = name[0]['name']
    dojo_ninjas = Ninja.get_dojo_ninjas(dojo_id)
    return render_template('dojo_show.html', dojo_ninjas = dojo_ninjas, dojo_name = dojo_name, dojo_id = dojo_id )

@app.route("/ninjas/new_ninja")
def new_ninja():
    all_dojos = Dojo.get_all()
    return render_template("new_ninja.html", all_dojos = all_dojos)

@app.route("/add_new_ninja", methods=["POST"])
def add_new_ninja():
    results = Ninja.save(request.form)
    dojo_id = request.form.get('dojo_id')
    return redirect(f"/dojos/get_one/{dojo_id}")

@app.route("/ninja/edit_ninja/<int:ninja_id>")
def edit_ninja(ninja_id):
    data = {
        "id" : ninja_id
    }
    all_dojos = Dojo.get_all()
    ninja = Ninja.get_ninja(data)
    ninja = ninja[0]
    dojo_id = ninja["dojo_id"]
    dojo_name = Dojo.get_dojo_name(dojo_id)
    dojo_name = dojo_name[0]['name']
    return render_template("edit_ninja.html", ninja = ninja, all_dojos = all_dojos, dojo_name = dojo_name)

@app.route("/save_updated_ninja/<int:ninja_id>", methods=["POST"])
def save_updated_ninja(ninja_id):
    ninja_id = {
        "ninja_id": ninja_id
    }
    dojo_id = request.form.get("dojo_id")
    result = Ninja.update(request.form, ninja_id)
    return redirect(f"/dojos/get_one/{dojo_id}")

@app.route("/ninja/delete_ninja/<int:ninja_id>/<int:dojo_id>")
def delete_ninja(ninja_id, dojo_id):
    Ninja.delete(request.form, ninja_id)
    return redirect(f"/dojos/get_one/{dojo_id}")