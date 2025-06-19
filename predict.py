import spacy

# Load the trained model
nlp_model = spacy.load("models/my_nlp_model")

# Test on new text
text = "This is an amazing experience!"
doc = nlp_model(text)

print(doc.cats)  # Output: {'POSITIVE': 0.95, 'NEGATIVE': 0.05}
