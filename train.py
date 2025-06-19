import spacy
from spacy.training.example import Example
import os

# Ensure the models directory exists
os.makedirs("models", exist_ok=True)

# Initialize blank NLP model
nlp = spacy.blank("en")

# Add text classification component with better optimization
text_cat = nlp.add_pipe("textcat_multilabel")  # Improved for handling imbalanced data
text_cat.add_label("POSITIVE")
text_cat.add_label("NEGATIVE")

# Expanded training dataset
train_data = [
    ("I love this product!", {"cats": {"POSITIVE": 1, "NEGATIVE": 0}}),
    ("This movie is terrible.", {"cats": {"POSITIVE": 0, "NEGATIVE": 1}}),
    ("Absolutely amazing experience!", {"cats": {"POSITIVE": 1, "NEGATIVE": 0}}),
    ("I hated every moment of this.", {"cats": {"POSITIVE": 0, "NEGATIVE": 1}}),
    ("Best decision ever!", {"cats": {"POSITIVE": 1, "NEGATIVE": 0}}),
    ("Worst thing I've bought.", {"cats": {"POSITIVE": 0, "NEGATIVE": 1}}),
]

# Train the model with more iterations
optimizer = nlp.begin_training()
for epoch in range(50):  # Increased epochs for better accuracy
    for text, annotations in train_data:
        example = Example.from_dict(nlp.make_doc(text), annotations)
        nlp.update([example], sgd=optimizer)

# Save the trained model
nlp.to_disk("models/my_nlp_model")
print("✅ Model trained and saved successfully!")
