from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

counter = 0

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/counter", methods=["GET"])
def get_counter():
    global counter
    return jsonify({"counter": counter})

@app.route("/increase", methods=["POST"])
def increase():
    global counter
    counter += 1
    return jsonify({"counter": counter})

@app.route("/decrease", methods=["POST"])
def decrease():
    global counter
    counter -= 1
    return jsonify({"counter": counter})

@app.route("/reset", methods=["POST"])
def reset():
    global counter
    counter = 0
    return jsonify({"counter": counter})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)