from flask import Flask

from controller.users_controller import get_all_users, get_all_users_json

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Main page</h1>"

@app.route("/users", methods=['GET'])
def get_users():
    return get_all_users_json()


if __name__ == '__main__':
    app.run(debug=True)
