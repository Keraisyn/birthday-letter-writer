import lettertools
import flask
from flask import request, jsonify, url_for, render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True


corpus, word_dict = lettertools.create_model()


@app.route("/", methods=["GET"])
def main():
    return render_template("index.html")


@app.route("/api", methods=["GET"])
def lettergenerator():
    if "words" in request.args:
        n_words = int(request.args["words"])
    else:
        n_words = 30

    generated_text = lettertools.create_chain(corpus, word_dict, n_words)

    generated_data = {"text": generated_text}

    return jsonify(generated_data)


app.run()
