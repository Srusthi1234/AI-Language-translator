from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

translator = pipeline(
    "translation",
    model="Helsinki-NLP/opus-mt-en-de"
)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/translate", methods=["POST"])
def translate():
    text = request.form["text"]

    result = translator(text)

    translated_text = result[0]["translation_text"]

    return render_template(
        "index.html",
        translated=translated_text
    )


if __name__ == "__main__":
    app.run(debug=True)