from flask_app import app
from flask_app.controllers import controllers_user

app.secret_key = "py is life"

if __name__ == "__main__":
    app.run(port=5001, debug=True)