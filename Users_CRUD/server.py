from flask import Flask, render_template, redirect, request, session
from user import User
app = Flask(__name__)
app.secret_key = "py is life"


@app.route("/")
def index():
    # call the get all classmethod to get all users
    all_users = User.get_all()
    return render_template("index.html", users = all_users)

@app.route('/user/create', methods=["POST"])
def create():
    User.save(request.form)
    return redirect(f'/show_users')

@app.route('/show_users')
def show_users():
    users = User.get_all()
    return render_template("show_users.html", all_users = users)

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


if __name__ == "__main__":
    app.run(port=5001, debug=True)