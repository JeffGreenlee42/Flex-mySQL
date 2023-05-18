# from flask_app import app
from flask import Flask, render_template, redirect, request, session
from flask_app.models.models_dojos import Dojos

@app.route("/")
def index():
    return render_template("dojo.html")
    
