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
    # session["first_name"] = request.form["first_name"]
    # session["last_name"] = request.form["last_name"]
    # session["email"] == request["email"]
    return redirect(f'/show_users')

@app.route('/show_users')
def show_users():
    users = User.get_all()
    return render_template("show_users.html", all_users = users)

@app.route(f'/user/update/<int:user_id>')
def update_user(user_id):
    print("Hello world!")
    print(f"User ID is {user_id}")
    data = {
        'id': user_id
    }
    print(f"printing data: {data}")
    user = User.get_one(data)
    print(f"print user: {user}")
    return render_template('update.html', item_id = user)

if __name__ == "__main__":
    app.run(port=5001, debug=True)


