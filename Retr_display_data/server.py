from flask import Flask, render_template, redirect, request
# import the class from friend.py
from friend import Friend
app = Flask(__name__)

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    all_friends = Friend.get_all()
    # print(friends)
    return render_template("index.html", friends = all_friends)

@app.route('/friends/create', methods=["POST"])
def create():
    # data = {
    #     "first_name": request.form["first_name"],
    #     "last_name":  request.form["last_name"],
    #     "occupation": request.form["occupation"]
    # }
    Friend.save(request.form)
    return redirect('/')

@app.route('/friend/show/<int:friend_id>')
def show(friend_id):
    friend = Friend.get_one(friend_id)
    return render_template("show_friend.html", friend=friend)

@app.route('/show_friends')
def show_friends():
    friends = Friend.get_all()
    print(friends)
    return render_template("show_friends.html", all_friends = friends)


if __name__ == "__main__":
    app.run(port=5001, debug=True)


