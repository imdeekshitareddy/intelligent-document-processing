from flask import Flask, render_template, request
import os

from utils.pdf_reader import extract_text_from_pdf
from model.entity_extractor import extract_entities

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():

    result = None

    if request.method == "POST":

        file = request.files["pdf"]

        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            text = extract_text_from_pdf(filepath)

            result = extract_entities(text)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)