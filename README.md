# NLP Text Classifier with spaCy + Flask

A simple yet effective sentiment analysis API built using [spaCy](https://spacy.io/), Flask, and custom training data. 
This project demonstrates how to train your own binary sentiment model (POSITIVE vs NEGATIVE) and serve it through an HTTP API.

---

## Features

- Trains a custom `textcat_multilabel` pipeline using spaCy
- Handles POSITIVE and NEGATIVE classification
- REST API powered by Flask (`/predict` endpoint)
- Example script to test the deployed API
- Modular codebase (`train.py`, `predict.py`, `app.py`, `test_api.py`)

---

## Project Structure

├── app.py # Flask server to serve prediction endpoint ├── train.py # Model training script (spaCy) ├── predict.py # Helper to load model and predict locally
├── test_api.py # Sends a POST request to the Flask API ├── requirements.txt # Required Python packages ├── models/ │ └── my_nlp_model/ # Saved custom-trained spaCy model └── README.md



## 📦 Setup Instructions

1. **Create virtual environment** (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate

2.Install dependencies:
pip install -r requirements.txt (If all together giving error, try installing one by one).

3. Train the model:
    python train.py

4. Run the Flask app:
    python app.py

5. python test_api.py


Example Prediction
POST to /predict with:
{
  "text": "This is an amazing experience!"
}


Response:

{
  "POSITIVE": 0.999,
  "NEGATIVE": 0.001
}

## 🙌 Acknowledgments

- [spaCy.io](https://spacy.io/) for the excellent NLP framework  
- The Python and open-source communities


 



