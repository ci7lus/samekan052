from flask import Flask, render_template, jsonify
from flask_cors import CORS
from makeSentence import makeSentence

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return render_template("index.html", sentence=makeSentence())


@app.route("/api")
def api():
    return jsonify(sentence=makeSentence())


if __name__ == "__main__":
    app.debug = True
    app.env = "DEV"
    app.run()
