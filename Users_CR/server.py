from flask import Flask, render_template, redirect, request, session
# import the class from users.py
from user import User
app = Flask(__name__)

@app.route("/")
def index():
    # call the get all classmethod to get all users
    all_users = User.get_all()
    return render_template("index.html", users = all_users)

@app.route('/user/create', methods=["POST"])
def create():
    User.save(request.form)
    session["first_name"] = request.formp["first_name"]
    session["last_name"] = request.form["last_name"]
    session["email"] == request["email"]
    return redirect(f'/show_users')

# @app.route('/user/show/<int:user_id>')
# def show(user_id):
#     user = User.get_one(user_id)
#     print(user.first_name)
#     return render_template("show_user.html", user=user)

@app.route('/show_users')
def show_users():
    users = User.get_all()
    return render_template("show_users.html", all_users = users)


if __name__ == "__main__":
    app.run(port=5001, debug=True)


