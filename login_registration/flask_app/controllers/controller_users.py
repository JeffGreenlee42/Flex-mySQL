from flask_app import app
from flask import Flask, render_template, redirect, request, session, flash
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
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password'],
        'password_confirmation': request.form['password_confirmation']
    }
    valid = User.validate_user(data)
    if valid:
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        data['pw_hash'] = pw_hash
        user = User.add_user(data)
        session['user_id'] = user
        return redirect("/dashboard")
    return redirect("/")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/login", methods=["POST"])
def login():
    if 'user_id' not in session:
        return redirect('/')
    user = User.get_by_email(request.form)
    if not user:
        flash("Invalid email or Password", "login")
        return redirect('/')
    # for re-populating email field if login fails
    if not bcrypt.check_password_hash(user.password, request.form['login_password']):
        flash("Invalid email or Password", "login")
        return redirect('/')
    session['user_id'] = user.id
    session['first_name'] = user.first_name
    session['last_name'] = user.last_name
    session['login_email'] = user.email
    return redirect("/dashboard")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
