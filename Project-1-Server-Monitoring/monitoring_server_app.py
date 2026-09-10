from flask import Flask , jsonify , render_template

import json

app = Flask(__name__)

@app.route("/")
def home():
    with open("server_history.json", "r") as file:
        old_data = json.load(file)
    server_list = old_data
    return server_list

@app.route("/data")
def data():
    with open("server_history.json", "r") as file:
        server_list = json.load(file)
    return jsonify(server_list)


@app.route("/test")
def test():
    return render_template("test.html")


if __name__ == '__main__':  
   app.run() 