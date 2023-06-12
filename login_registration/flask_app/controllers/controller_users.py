from flask_app import app
from flask import Flask, render_template, redirect, request, session
from flask_app.models.model_user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/")
def index():
    if len(session) < 1:
        session['user_id'] = ""
        session['first_name'] = ""
        session['last_name'] = ""
        session['email'] = ""
        session['login_email'] = ""
    return render_template('index.html')

@app.route("/register", methods=["POST"])
def register():
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    if not User.validate_user(request.form):
        return redirect("/")
    print(f"request.form['password'] is {request.form['password']}")
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash
    }
    User.add_user(data)
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/login", methods=["POST"])
def login():
    session['login_email'] = request.form['login_email']
    data = {
        'email': request.form['login_email'],
        'password': request.form['login_password']
    }
    print("We are in route Login")
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        return redirect("/")
    session['user_id'] = user_in_db.id
    return redirect("/dashboard")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
