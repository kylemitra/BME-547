from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route("/", methods=["GET"])
def server_status():
    return "My server is on."


@app.route("/time", methods=["GET"])
def time():
    return str(datetime.now().time())


@app.route("/date", methods=["GET"])
def date():
    return str(datetime.now().date())


@app.route("/age", methods=["POST"])
def age():
    in_data = request.get_json()
    date = in_data['date']
    units = in_data['units']
    difference = datetime.now() - date
    return difference


@app.route("/until_next_meal/<meal>", methods=["GET"])
def time_until_next_meal(meal): # Incomplete
    breakfast = datetime()
    lunch = datetime
    dinner = datetime
    return meal - datetime.now()


if __name__ == '__main__':
    app.run()
