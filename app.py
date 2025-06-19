from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)
nlp_model = spacy.load("models/my_nlp_model")


@app.route("/")
def home():
    return "Flask NLP API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["text"]
    doc = nlp_model(data)
    return jsonify(doc.cats)

if __name__ == "__main__":
    app.run(debug=True)
