from flask_app import app
from flask import Flask, render_template, redirect, request, session
from flask_app.models.models_user import User



@app.route("/")
def index():
    users = User.get_all()
    return render_template("show_users.html", all_users = users)

@app.route("/add_new_user")
def add_new_user():
    return render_template("index.html")


@app.route('/user/create', methods=["POST"])
def create():
    user_id = User.save(request.form)
    # return redirect(f'/show_users')
    # print(f"The passed user ID from addUser is: {user}")
    return redirect(f'/user/show_one_user/{user_id}')

# @app.route('/user/create', methods=["POST"])
# def create():
#     User.save(request.form)
#     return redirect(f'/show_users')

@app.route('/show_users')
def show_users():
    users = User.get_all()
    return render_template("show_users.html", all_users = users)

@app.route('/user/show_one_user/<int:user_id>')
def show_one_user(user_id):
    data = {
        'id': user_id
    }
    user = User.get_one(data)
    return render_template('one_user.html', user = user)


@app.route('/user/update/<int:user_id>')
def update_user(user_id):
    # print(f"at line 27 user_id is {user_id}")
    data = {
        'id': user_id
    }
    user = User.get_one(data)
    return render_template('update.html', user = user)


@app.route('/user/save_updated_user/<int:user_id>', methods=['POST'])
def save_updated_user(user_id):
    # data = {
    #     'id': user_id
    # }
    User.update(request.form, user_id)
    return redirect("/show_users")

@app.route('/user/delete_user/<int:user_id>')
def delete_user(user_id):
    User.delete(request.form, user_id)
    return redirect("/show_users")

