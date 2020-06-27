from flask import Flask, render_template, jsonify
import markovify
import MeCab

app = Flask(__name__)


@app.route("/")
def index():
    with open("dist/model.json", "r") as f:
        textModel = markovify.Text.from_json(f.read())

    while True:
        made = textModel.make_sentence(tries=100)

        if made:
            sentence = "".join(made.split())
            break

    return render_template("index.html", sentence=sentence)
