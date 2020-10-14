from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def server_status():
    return "My server is on."


@app.route("/info", methods=["GET"])
def info():
    info_string = "Here is where I might share usage information"
    return info_string


@app.route("/add", methods=["POST"])
def add_function():
    """
    dict = {"a": int, "b": int}
    """
    in_data = request.get_json()
    print(type(in_data))
    answer = in_data["a"] + in_data["b"]
    return_list = [answer, "correct"]
    if answer < 0:
        return 'No negative numbers', 400  # 400 is the status code to be returned
    else:
        return jsonify(return_list)  # jsonify must be used in a return call
    # return "The answer is {}".format(answer)


#  This stores whatever you type in name in the URL as the variable name
@app.route("/say_hello/<name>", methods=["GET"])
def say_hello(name):
    return "Hello, {}".format(name)


@app.route("/add_numbers/<a>/<b>", methods=["GET"])
def say_hello(a, b):
    x = int(a) + int(b)
    return "Answer is {}".format(x)


if __name__ == '__main__':
    app.run()
